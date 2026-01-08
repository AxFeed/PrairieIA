# ashGen
import random
import pandas as pd


def generate(n, chanceBonneReponse = 100):
    ash_keys = ['a', 'b', 'c', 'd', 'v', '1', '2', '3', 'ref']  # les colonnes de mon df
    df = pd.DataFrame(columns=ash_keys)  # créer le df
    trompage = 0

    for i in range(n):  # n fois
        bars = set()  # un set, c'est (presque) comme un tableau, mais sans doublon
        while len(bars) < 3:  # je crée les 3 barres.
            bars.add(random.randrange(1, 11))  # Comme c'est un set, il ne peut pas y avoir deux barres de la même
                                                            # taille,
            # je mets un while car je dois créer des barres jusqu'à ce que j'en aie 3

        bars = list(bars)  # je transforme en list c'est plus pratique qu'un set
        bonne_reponse = random.randrange(1, 4)  # choisir au hasard une barre
        ref = bars[bonne_reponse - 1]  # mettre la même taille à la ref

        if random.random() < chanceBonneReponse / 100:
            choix_des_complices = bonne_reponse
        else:
            choix_des_complices = random.randrange(1,
                                               4)  # pour les complices il ne faut pas qu'ils choisissent la bonne
                                                        # réponse !
            while bars[choix_des_complices - 1] == ref:  # donc, je choisi au hasard jusqu'à ce que ce soit faux
                choix_des_complices = random.randrange(1, 3)
            trompage += 1

        ligne = [
            choix_des_complices,  # a
            choix_des_complices,  # b
            choix_des_complices,  # c
            choix_des_complices,  # d,
            None,  # v
            bars[0],  # 1
            bars[1],  # 2
            bars[2],  # 3
            ref  # ref
        ]
        autre_df = pd.DataFrame([ligne], columns=ash_keys)

        df = pd.concat([df, autre_df])

    if chanceBonneReponse != 100:
        print("On a fait exprès de se tromper", trompage , "fois sur", n, "générations !")

    return df


if __name__ == "__main__":
    df = generate(10, 100)
    print(df)