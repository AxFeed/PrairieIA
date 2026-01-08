# Documentation du code de génération et d'entraînement d'un arbre de décision

Ce code permet de **générer des données**, **d’y ajouter du bruit**, puis **d’entraîner un arbre de décision** afin d’évaluer ses performances en fonction du taux d’erreur dans les données d’apprentissage.

Il est composé de **trois parties principales** :

- `main` : script principal qui entraîne et évalue le modèle
- `ashGen` : générateur de données (avec ou sans bruit)
- `solver` : solveur qui calcule la bonne réponse théorique

---

## Script principal : `main`

Ce script orchestre l’ensemble du programme : génération des données, entraînement du modèle, évaluation et affichage des résultats.

### Fonctionnement global

1. Demande à l’utilisateur :
   - le nombre de données d’entraînement
   - le nombre de données de test
2. Génère un **jeu de test propre** (100 % de bonnes réponses)
3. Fait varier le **taux de bonnes réponses** dans les données d’entraînement
4. Entraîne un **arbre de décision**
5. Compare les prédictions du modèle avec la solution réelle
6. Trace :
   - l’arbre de décision
   - un graphique de performance du modèle

---

### Détail du fonctionnement

1. Génération du DataFrame de test sans bruit  
2. Boucle tant que le taux de bonnes réponses n’a pas dépassé 100 %  
3. Génération d’un DataFrame d’entraînement avec bruit  
4. Création et entraînement de l’arbre de décision (`DecisionTreeClassifier`)  
5. Affichage de l’arbre de décision  
6. Prédiction sur le jeu de test  
7. Calcul du pourcentage de réussite  
8. Stockage des résultats pour affichage graphique  
9. Tracé de la courbe de performance finale  

---

### Données utilisées par le modèle

Colonnes utilisées en entrée :

- `a`, `b`, `c`, `d` : réponses des complices  
- `1`, `2`, `3` : tailles des barres  
- `ref` : valeur de référence  

Colonne de sortie :

- `v` : bonne réponse  

---

## Générateur de données : `ashGen`

### Fonction : `generate(n, chanceBonneReponse=100)`

Cette fonction génère un **DataFrame de données simulées** représentant des choix effectués par des complices, avec la possibilité d’introduire des erreurs.

---

### Paramètres

- `$n` : nombre de lignes à générer  
- `$chanceBonneReponse` : pourcentage de chance que les complices donnent la bonne réponse (ex : `80`)  

---

### Fonctionnement

1. Création d’un DataFrame vide avec les colonnes :
   - `a`, `b`, `c`, `d`, `v`, `1`, `2`, `3`, `ref`
2. Pour chaque ligne :
   - Génère 3 barres de tailles différentes  
   - Choisit aléatoirement la bonne réponse  
   - Définit une référence (`ref`)  
3. Selon la probabilité donnée :
   - soit les complices donnent la bonne réponse  
   - soit ils donnent volontairement une mauvaise réponse  
4. Ajoute la ligne au DataFrame  
5. Affiche le nombre de tromperies si le taux n’est pas à 100 %  

---

### Exemple

```python
df = generate(100, 80)
```

Cela génère 100 lignes avec 80 % de bonnes réponses et 20 % d’erreurs volontaires.

## Solveur : `solver`

Cette classe permet de calculer la bonne réponse théorique à partir des données.

### Fonction : solve(line)

Retourne la bonne réponse en comparant la référence (ref) aux tailles des barres.

### Fonctionnement

1.Compare la valeur de ref avec :
  - la barre 1
  - la barre 2
  - sinon la barre 3
2. Retourne le numéro correspondant à la bonne barre

### Fonction : solveDf(df)

Applique la fonction solve à toutes les lignes d’un DataFrame et remplit la colonne v.

### Exemple
solveDf(df)

Ajoute automatiquement la colonne v au DataFrame.

## Résultat final

Le programme permet de :

- Visualiser l’impact du bruit dans les données d’entraînement
- Observer la robustesse de l’arbre de décision
- Analyser la performance du modèle en fonction du taux d’erreur