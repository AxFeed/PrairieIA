import random
from itertools import product
from Player import Player
from Strategies import Strategies
from Dataframe import Dataframe
import seaborn as sns
import matplotlib.pyplot as plt

strategiesList = ["random", "low", "high", "semi-optimal (Pas la smart)"]

# On joue une partie et renvoie True si le robot à gagné
def playCardGame(human_strategy, robot_strategy):
    mancheRobot = 0

    # On fait 5 manches
    for i in range(5):

        # On utilise notre méthode pour récupérer l'index de la carte à jouer pour l'humain
        cardHuman = Strategies.choose(
            Strategies,
            human_strategy,
            "human",
            human.cards,
            ordi.cards
        )

        # On utilise notre méthode pour récupérer l'inde de la carte à jour pour le robot
        cardOrdi = Strategies.choose(
            Strategies,
            robot_strategy,
            "ordi",
            human.cards,
            ordi.cards
        )

        if cardOrdi.value >= cardHuman.value:
            mancheRobot += 1

        human.cards.remove(cardHuman)
        ordi.cards.remove(cardOrdi)

    return mancheRobot >= 3

# Liste de toutes les combinaisons de stratégies possibles
all_tests = list(product(strategiesList, repeat=2))

winrates = []

nbGames = 1000000

# On va jouer toutes les combinaisons possible
for human_strategy, robot_strategy in all_tests:
    robotWin = 0

    # On va simuler X partie
    for i in range(nbGames):
        # J'initialise mes joueurs avec leurs cartes
        players = Player.createPlayers(Player)
        human = players[0]
        ordi = players[1]

        # On joue notre partie et si le robot a gagné on incrémente
        if playCardGame(human_strategy, robot_strategy):
            robotWin += 1

    winrate = robotWin / nbGames
    winrates.append(winrate)

    print(human_strategy, "vs", robot_strategy, "→ winrate robot :", winrate)


# On créer notre DataFrame
df = Dataframe.generate(Dataframe, strategiesList, winrates)
print(df)

# annot=True pour afficher les valeurs
# fmt=.2f pour mettre les résultats sous forme décimale avec X nombres derrières la virgule
# cmap Pour la couleur
plt.figure(figsize=(8, 6))  # taille de la figure
sns.heatmap(df, annot=True, fmt=".6f", cmap="YlGnBu")
plt.title("Winrate du robot selon les stratégies")
plt.xlabel("Stratégie du robot")
plt.ylabel("Stratégie de l'humain")
plt.show()
