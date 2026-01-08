# main
from ashGen import generate
from solver import solve, solveDf
from joblib import dump, load


df = generate(1, 100)
result = solve(df.loc[0])

generateRight = 100
generateWrong = 500
df = generate(generateRight, 100)

solved = solveDf(df)


from sklearn import tree
import matplotlib.pyplot as plt

inputs = df[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df[['v']]
arbre = tree.DecisionTreeClassifier()

arbre = arbre.fit(inputs, output)
tree.plot_tree(arbre)
plt.figure(figsize=(30,15))  # plus grand pour mieux voir

# Tracer l'arbre
tree.plot_tree(
    arbre,
    filled=True,                 # colore les nœuds selon la classe
    feature_names=inputs.columns, # noms des colonnes
    class_names=True,             # noms des classes
    rounded=True,                 # coins arrondis
    proportion=True,              # montre proportion de chaque classe dans le nœud
    fontsize=12                   # taille du texte
)

# Afficher
plt.show()


dfTest = generate(2, 100)
print(dfTest)

# Générer un DataFrame test de n lignes
dfTest = generate(generateWrong, 100).reset_index(drop=True)  # ici 10 lignes

# Prédictions pour toutes les lignes en une seule fois
repArbre = arbre.predict(dfTest[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']])

repSolver = dfTest.apply(solve, axis=1)

print("Arbre  :", repArbre)
print("Solve  :", repSolver.values)

dump(arbre, 'arbre.joblib')

ok = 0
wrongTab = []

for i in range(len(repArbre)):
    if repArbre[i] == repSolver.iloc[i]:
        ok = ok + 1
    else:
        wrongTab.append([int(repSolver.iloc[i]), int(repArbre[i])])

pourcentage = (ok / len(repArbre))*100
print("Pour ", generateRight, "données d'entrainement, et ", generateWrong, "données test, le pourcentage de fiabilité est de : ", pourcentage, "%")

print("Données erronées :", wrongTab)