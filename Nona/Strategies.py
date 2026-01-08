#Strategies.py
import random

class Strategies:
    def __init__(self):
        self = self

    # Renvoi l'index de la carte à utiliser selon la stratégie choisie
    def choose(self, choix, player, humanCards, ordiCards):

        match choix:
            # Joue une carte random
            case "random":

                if player == "human":
                    rnd = random.randrange(len(humanCards))
                    return humanCards[rnd]
                else:
                    rnd = random.randrange(len(ordiCards))
                    return ordiCards[rnd]
            # Joue la carte la plus grande
            case "high":
                if player == "human":
                    return max(humanCards, key=lambda c: c.value)
                else:
                    return max(ordiCards, key=lambda c: c.value)
            # Joue la carte la plus petite
            case "low":
                if player == "human":
                    return min(humanCards, key=lambda c: c.value)
                else:
                    return min(ordiCards, key=lambda c: c.value)
            # Si voit que les cartes sont plus petite joue la plus grande, sinon joue la plus petite
            case "semi-optimal (Pas la smart)":
                if player == "human":
                    if max(humanCards, key=lambda c: c.value).value > max(ordiCards, key=lambda c: c.value).value:
                        return max(humanCards, key=lambda c: c.value)
                    else:
                        return min(humanCards, key=lambda c: c.value)
                else:
                    if max(ordiCards, key=lambda c: c.value).value >= max(humanCards, key=lambda c: c.value).value:
                        return max(ordiCards, key=lambda c: c.value)
                    else:
                        return min(ordiCards, key=lambda c: c.value)
            # Cas nominal ou la stratégie n'existe pas
            case _:
                print("Stratégie inconnue")
