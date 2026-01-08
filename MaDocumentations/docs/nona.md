# Documentation du projet de simulation de jeu de cartes et stratégies

Ce projet simule un **jeu de cartes simple entre un humain et un robot**, en testant différentes **stratégies de jeu** afin d’analyser le **taux de victoire du robot** selon la stratégie utilisée par chaque joueur.

Le programme permet de :
- simuler un grand nombre de parties
- tester toutes les combinaisons de stratégies possibles
- calculer les winrates
- afficher les résultats sous forme de **heatmap**

---

## Architecture du projet

Le projet est composé des modules suivants :

- `Card` : gestion des cartes et de la distribution
- `Player` : création des joueurs
- `Strategies` : définition des stratégies de jeu
- `Dataframe` : création du tableau de résultats
- Script principal : simulation et affichage des résultats

---

## Gestion des cartes : `Card`

### Classe : `Card`

Cette classe représente une carte et contient les méthodes liées à la création du jeu et à la distribution.

---

### Attributs

- `suit` : couleur de la carte (`"C"` ou `"R"`)
- `value` : valeur numérique de la carte

---

### Méthode : `createSet()`

Crée le jeu de cartes.

---

### Fonctionnement

1. Crée 5 cartes de couleur `"C"` avec des valeurs de `0` à `4`
2. Crée 5 cartes de couleur `"R"` avec des valeurs de `1` à `5`
3. Retourne la liste complète des cartes

---

### Méthode : `distribute()`

Distribue les cartes aléatoirement entre le joueur humain et le robot.

---

### Fonctionnement

1. Récupère le jeu de cartes
2. Tire alternativement une carte aléatoire pour l’humain et pour le robot
3. Continue jusqu’à épuisement du paquet
4. Retourne un tableau contenantles cartes du joueur humain et les cartes du robot

---

## Gestion des joueurs : `Player`

### Classe : `Player`

Représente un joueur du jeu (humain ou robot).

---

### Attributs

- `name` : nom du joueur
- `cards` : liste des cartes du joueur

---

### Méthode : `createPlayers()`

Crée les deux joueurs de la partie.

---

### Fonctionnement

1. Distribue les cartes via la classe `Card`
2. Crée un joueur humain et un joueur robot
3. Retourne la liste des deux joueurs

---

## Gestion des stratégies : `Strategies`

### Classe : `Strategies`

Cette classe contient les différentes stratégies possibles pour choisir une carte à jouer.

---

### Méthode : `choose(choix, player, humanCards, ordiCards)`

Retourne la carte à jouer selon la stratégie choisie.

---

### Paramètres

- `$choix` : nom de la stratégie
- `$player` : `"human"` ou `"ordi"`
- `$humanCards` : cartes du joueur humain
- `$ordiCards` : cartes du robot

---

### Stratégies disponibles

- `random` : joue une carte aléatoire
- `high` : joue la carte avec la plus grande valeur
- `low` : joue la carte avec la plus petite valeur
- `semi-optimal (Pas la smart)` : joue la plus grande carte si elle est supérieure à celle de l’adversaire SINON joue la plus petite

---

## Simulation du jeu

### Fonction : `playCardGame(human_strategy, robot_strategy)`

Simule une partie complète entre un humain et un robot.

---

### Fonctionnement

1. Joue 5 manches
2. À chaque manche : chaque joueur choisit une carte selon sa stratégie => la carte du robot gagne si sa valeur est supérieure ou égale
3. Le robot gagne la partie s’il remporte au moins 3 manches
4. Retourne `True` si le robot gagne, sinon `False`

---

## Simulation massive et analyse

### Fonctionnement global

1. Liste toutes les combinaisons possibles de stratégies
2. Simule un grand nombre de parties pour chaque combinaison
3. Calcule le **winrate du robot**
4. Stocke les résultats
5. Affiche les résultats sous forme de tableau et de heatmap

---

### Paramètres importants

- `nbGames` : nombre de parties simulées par combinaison (ex : `1_000_000`)
- `strategiesList` : liste des stratégies testées

---

## Création du DataFrame : `Dataframe`

### Classe : `Dataframe`

Permet de créer un DataFrame pandas contenant les winrates.

---

### Méthode : `generate(keys, winrate)`

Construit le tableau des résultats.

---

### Fonctionnement

1. Crée un DataFrame avec => lignes : stratégie de l’humain et colonnes : stratégie du robot
2. Remplit les cellules avec les winrates calculés
3. Convertit les valeurs en float
4. Retourne le DataFrame final

---

## Visualisation des résultats

Les résultats sont affichés sous forme de **heatmap** grâce à `seaborn`.

- Les valeurs représentent le **taux de victoire du robot**
- Plus la valeur est élevée, plus la stratégie est efficace pour le robot

---

## Conclusion

Ce projet permet de :

- comparer différentes stratégies de jeu
- observer leur efficacité statistique
- visualiser clairement les résultats
- analyser l’avantage stratégique du robot selon le comportement humain

---
