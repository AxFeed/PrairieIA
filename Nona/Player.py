#player.py

from Card import Card

class Player:
    def __init__(self, name: str, cards):
        self.name = name
        self.cards = cards

    # Créer les deux joueurs (Humain vs Robot)
    def createPlayers(self):

        cardsSet = Card.distribute(Card)
        players = []

        human = Player("Human", cardsSet[0])
        ordi = Player("Ordi", cardsSet[1])

        players.append(human)
        players.append(ordi)

        return players


    def __str__(self):
        return self.name + ": " + str([str(Card) for Card in self.cards])