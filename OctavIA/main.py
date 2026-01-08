# main
from ashGen import generate
from solver import solve, solveDf
from joblib import dump
from sklearn import tree
import matplotlib.pyplot as plt

nbGenerate = int(input("Combien voulez vous générer de cas d'apprentissage ? "))
nbGenerateTest = int(input("Combien voulez vous générer de cas de test ? "))
chanceBonneReponse = 0
tabPourcentage = []
tabChance = []

# On créer un DataFrame de test propre (réponses vraies)
dfTest = generate(nbGenerateTest, 100)
solveDf(dfTest)

while chanceBonneReponse != 105:
    # On génére notre DataFrame d’entrainement AVEC bruit
    df = generate(nbGenerate, chanceBonneReponse)
    solveDf(df)

    # On créer notre arbre de décision
    inputs = df[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
    output = df[['v']]
    arbre = tree.DecisionTreeClassifier()

    # On l'entraine
    arbre = arbre.fit(inputs, output)

    # Si jamais ou veut afficher l'arbre de décision du modèle
    """"
    tree.plot_tree(arbre)

    plt.figure(figsize=(30,15))  # plus grand pour mieux voir

    #Tracer l'arbre
    tree.plot_tree(
    arbre,
    filled=True,                 # colore les nœuds selon la classe
    feature_names=inputs.columns, # noms des colonnes
    class_names=True,             # noms des classes
    #rounded=True,                 # coins arrondis
    proportion=True,              # montre proportion de chaque classe dans le nœud
    fontsize=12                   # taille du texte
    )

    # Afficher
    plt.show()
    """


    # Prédictions pour toutes les lignes en une seule fois (sur test propre)
    repArbre = arbre.predict(dfTest[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']])
    repSolver = dfTest.apply(solve, axis=1)

    # Si on veut enregistrer notre modèle
    # dump(arbre, 'arbre.joblib')

    ok = 0
    for i in range(len(repArbre)):
        if repArbre[i] == repSolver.iloc[i]:
            ok += 1

    pourcentage = (ok / len(repArbre)) * 100
    print("Pour", nbGenerate, "données d'entrainement avec", chanceBonneReponse, "% de bonnes réponses, le pourcentage de réussite est de :", pourcentage, "%")

    tabPourcentage.append(pourcentage)
    tabChance.append(chanceBonneReponse)

    chanceBonneReponse += 5

plt.figure(figsize=(10, 6))
plt.plot(tabChance, tabPourcentage, marker='o', linestyle='-', color='blue')
plt.xlabel("Chance de bonne réponse dans l'entraînement (%)")
plt.ylabel("Pourcentage de réussite du modèle (%)")
title = "Performance du modèle en fonction du taux d'erreur dans l'entraînement (", nbGenerate, "entrainement", nbGenerateTest, "tests )"
plt.title(title)
plt.grid(True)
plt.show()
