# main
from ashGen import generate
from solver import solve, solveDf
from joblib import dump, load


df = generate(1)
result = solve(df.loc[0])

generateRight = 1
generateWrong = 1000
df = generate(generateRight)

solved = solveDf(df)


from sklearn import tree
import matplotlib.pyplot as plt

inputs = df[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df[['v']]
arbre = tree.DecisionTreeClassifier()

arbre = arbre.fit(inputs, output)
tree.plot_tree(arbre)


dfTest = generate(2)
print(dfTest)

# Générer un DataFrame test de n lignes
dfTest = generate(generateWrong).reset_index(drop=True)  # ici 10 lignes

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