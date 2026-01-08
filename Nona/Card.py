#card.py

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #Créer la pioche
    def createSet(self):

        cards = []
        for i in range(5):
            card = Card("C", i)
            cards.append(card)

        for i in range(5):
            card = Card("R", i+1)
            cards.append(card)
        return cards

    # Distribue les cartes
    def distribute(self):
        cards = self.createSet(self)
        cardsPlayer = []
        cardsRobot = []
        cardGame = []

        while len(cards) > 0:
            rnd = random.randrange(len(cards))  # safer than randint
            cardsPlayer.append(cards.pop(rnd))

            if len(cards) == 0:
                break

            rnd = random.randrange(len(cards))
            cardsRobot.append(cards.pop(rnd))

        cardGame.append(cardsPlayer)
        cardGame.append(cardsRobot)

        return cardGame

    def __str__(self):
        return str(self.suit) + str(self.value)





