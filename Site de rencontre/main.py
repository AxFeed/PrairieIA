import json
import unicodedata
import math
import numpy as np
from datetime import datetime
from pprint import pprint
from termcolor import colored

with open('people.json', 'r', encoding="utf-8") as p:
    people = json.loads(p.read())
    

print(colored("""
$$$$$$$$\\        $$\\           $$\\                           $$\\                               
\\__$$  __|       \\__|          $$ |                          $$ |                              
   $$ | $$$$$$\\  $$\\ $$$$$$$\\  $$ |  $$\\  $$$$$$\\   $$$$$$\\  $$ | $$$$$$\\ $$\\    $$\\  $$$$$$\\  
   $$ |$$  __$$\\ $$ |$$  __$$\\ $$ | $$  |$$  __$$\\ $$  __$$\\ $$ |$$  __$$\\\\$$\\  $$  |$$  __$$\\ 
   $$ |$$ |  \\__|$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \\__|$$ |$$ /  $$ |\\$$\\$$  / $$$$$$$$ |
   $$ |$$ |      $$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      $$ |$$ |  $$ | \\$$$  /  $$   ____|
   $$ |$$ |      $$ |$$ |  $$ |$$ | \\$$\\ \\$$$$$$$\\ $$ |$$\\   $$ |\\$$$$$$  |  \\$  /   \\$$$$$$$\\ 
   \\__|\\__|      \\__|\\__|  \\__|\\__|  \\__| \\_______|\\__|\\__|  \\__| \\______/    \\_/     \\_______|
================================================================================================
   
""", 'yellow'))
print(colored('Modele des données :', 'yellow'))
pprint(people[0])

# debut de l'exo
print(colored(''.join(['_' for _ in range(80)]), 'green', 'on_green'))

print(colored("Nombre d'hommes : ", 'yellow'))
# pour chaque personne du tableau, si son genre == 'Male' je le met dans le tableau hommes
hommes = [p for p in people if p['gender'] == 'Male']
# len() revoie la taille (nombre d'élément) d'un tableau
pprint(len(hommes))

################################################################################

# je peux aussi l'écrire avec une boucle classique
hommes2 = []                        # un tableau vide
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme (2-266-02250-4)
        hommes2.append(person)      # je l'ajoute au tableau
print(len(hommes2))

################################################################################

# je peux aussi l'écrire avec une boucle classique
femmes = []                        # un tableau vide
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Female":  # si c'est un homme (2-266-02250-4)
        femmes.append(person)      # je l'ajoute au tableau
print(len(femmes))

################################################################################

# dans la même idée, plutot que de mettre tous les hommes dans un tableau
# puis afficher la longueur du tableau, je peux juste les compter dans une variable
nb_hommes = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme
        nb_hommes = nb_hommes + 1   # j'ajoute 1 à mon compteur
print(nb_hommes)

################################################################################

print(colored("Nombre de femmes : ", 'yellow'))
# je peux compter les femmes ou calculer : nombre d'élement dans people - nombre d'homme
pnb_femmes = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Female":  # si c'est un homme
        pnb_femmes = pnb_femmes + 1   # j'ajoute 1 à mon compteur
print(pnb_femmes)

################################################################################

print(colored("Nombre de personnes qui cherchent un homme :", 'yellow'))
search_homme = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["looking_for"] == "M":  # si c'est un homme
        search_homme = search_homme + 1   # j'ajoute 1 à mon compteur
print(search_homme)

################################################################################

print(colored("Nombre de personnes qui cherchent une femme :", 'yellow'))
search_femme = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["looking_for"] == "F":  # si c'est un homme
        search_femme = search_femme + 1   # j'ajoute 1 à mon compteur
print(search_femme)

################################################################################

print(colored("Nombre de personnes qui gagnent plus de 2000$ :", 'yellow'))
number_over_2000 = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    income = float(person["income"].replace("$", ""))
    if income > 2000:  # si c'est un homme
        number_over_2000 = number_over_2000 + 1   # j'ajoute 1 à mon compteur
print(number_over_2000)

################################################################################

print(colored("Nombre de personnes qui aiment les Drama :", 'yellow'))
# là il va falloir regarder si le chaine de charactères "Drama" se trouve dans "pref_movie"
search_drama = sum(1 for person in people if "Drama" in person["pref_movie"].split("|"))
print(search_drama)

################################################################################

print(colored("Nombre de femmes qui aiment la science-fiction :", 'yellow'))
# si j'ai déjà un tableau avec toutes les femmes, je peux chercher directement dedans ;)
search_sf = 0                       # je commence à 0
search_sf = sum(1 for femme in femmes if "Sci-Fi" in femme["pref_movie"].split("|"))
print(search_sf)

################################################################################

print(colored('LEVEL 2' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$", 'yellow'))
for person in people:               # pour chaque persone du tableau
    income = float(person["income"].replace("$", ""))
    if income > 1482:  # si c'est un homme
        number = sum(1 for person in people if "Documentary" in person["pref_movie"].split("|"))
print(number)

################################################################################

print(colored("Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$", 'yellow'))
persons = []
for person in people:               # pour chaque persone du tableau
    income = float(person["income"].replace("$", ""))
    if income > 4000:  # si c'est un homme
        persons.append("Nom : " + person["last_name"] + " Prénom : " + person["first_name"] + " ID : " + str(person["id"]) + " Revenues : " + person["income"])
print(persons)

################################################################################

print(colored("Homme le plus riche (nom et id) :", 'yellow'))
plus_riche = max(hommes2, key=lambda x: float(x["income"].replace("$", "")))
print(str(plus_riche["id"]) + " " + plus_riche["last_name"])

################################################################################

print(colored("Salaire moyen :", 'yellow'))
total_income = 0
for person in people:               # pour chaque persone du tableau
    income = float(person["income"].replace("$", ""))
    total_income = total_income+income
print(str(total_income/len(people)))

################################################################################

print(colored("Salaire médian :", 'yellow'))
incomes = []
for person in people:               # pour chaque persone du tableau
    incomes.append(float(person["income"].replace("$", "")))
print(np.median(incomes))

################################################################################

print(colored("Nombre de personnes qui habitent dans l'hémisphère nord :", 'yellow'))
nb = 0
for person in people:               # pour chaque persone du tableau
    if person["latitude"] > 0:
        nb = nb +1
print(nb)

################################################################################

print(colored("Salaire moyen des personnes qui habitent dans l'hémisphère sud :", 'yellow'))
total_income = 0
total_sud = 0
for person in people:               # pour chaque persone du tableau
    if person["latitude"] < 0:
        income = float(person["income"].replace("$", ""))
        total_income = total_income+income
        total_sud = total_sud + 1
print(str(total_income/total_sud))

################################################################################

print(colored('LEVEL 3' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Personne qui habite le plus près de Bérénice Cawt (nom et id) :", 'yellow'))

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # rayon de la Terre en km

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    return R * c

for person in people:
    if person["first_name"] == "Bérénice" and person["last_name"] == "Cawt":
        berenice = person
    
closest_person = None
min_distance = float("inf")

for person in people:
    if person["id"] == berenice["id"]:
        continue  # on ignore Bérénice elle-même

    distance = haversine(
        berenice["latitude"], berenice["longitude"],
        person["latitude"], person["longitude"]
    )

    if distance < min_distance:
        min_distance = distance
        closest_person = person

print(str(closest_person["id"]) + " " + closest_person["last_name"])


################################################################################

print(colored("Personne qui habite le plus près de Ruì Brach (nom et id) :", 'yellow'))
for person in people:
    if person["first_name"] == "Ruì" and person["last_name"] == "Brach":
        Ruì = person
    
closest_person = None
min_distance = float("inf")

for person in people:
    if person["id"] == Ruì["id"]:
        continue  # on ignore Bérénice elle-même

    distance = haversine(
        Ruì["latitude"], Ruì["longitude"],
        person["latitude"], person["longitude"]
    )

    if distance < min_distance:
        min_distance = distance
        closest_person = person

print(str(closest_person["id"]) + " " + closest_person["last_name"])

################################################################################

print(colored("les 10 personnes qui habitent les plus près de Josée Boshard (nom et id) :", 'yellow'))
closests = []

for person in people:
    if person["first_name"] == "Josée" and person["last_name"] == "Boshard":
        josee = person
        
for person in people:
    if person["id"] == josee["id"]:
        continue

    distance = haversine(
        josee["latitude"], josee["longitude"],
        person["latitude"], person["longitude"]
    )

    if len(closests) < 10:
        closests.append((person["id"], person["last_name"]))
    else:
        # Chercher le plus grand distance dans la liste
        max_index = 0
        for i in range(1, 10):
            if closests[i][0] > closests[max_index][0]:
                max_index = i
        # Remplacer si la distance est plus petite
        if distance < closests[max_index][0]:
            closests[max_index] = ((person["id"], person["last_name"]))
      
print(closests)

################################################################################

print(colored("Les noms et ids des 23 personnes qui travaillent chez google :", 'yellow'))
googles = []
for person in people:
    if "google" in person["email"]:
        googles.append((person["id"], person["last_name"]))
  
print(googles)
        
################################################################################

print(colored("Personne la plus agée :", 'yellow'))

oldest_person = None

for person in people:
    if oldest_person is None:
        oldest_person = person
    else:
        if person["date_of_birth"] < oldest_person["date_of_birth"]:
            oldest_person = person
            
print(str(oldest_person["id"]) + " " + oldest_person["last_name"])

################################################################################

print(colored("Personne la plus jeune :", 'yellow'))

youngest_person = None

for person in people:
    if youngest_person is None:
        youngest_person = person
    else:
        if person["date_of_birth"] > youngest_person["date_of_birth"]:
            youngest_person = person
            
print(str(youngest_person["id"]) + " " + youngest_person["last_name"])

################################################################################

print(colored("Moyenne des différences d'age :", 'yellow'))

total_diff = 0
count = 0

for i in range(len(people)):
    date_i = datetime.strptime(people[i]["date_of_birth"], "%Y-%m-%d")
    
    for j in range(i + 1, len(people)):
        date_j = datetime.strptime(people[j]["date_of_birth"], "%Y-%m-%d")
        
        diff_jour = abs((date_i - date_j).days)
        diff_annee = diff_jour / 365.25
        
        total_diff += diff_annee
        count += 1

moyenne = total_diff / count

print(moyenne)

################################################################################

print(colored('LEVEL 4' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
print(colored("Genre de film le plus populaire :", 'yellow'))

film_counts = {}
for person in people:
    if "|" in person["pref_movie"]:
        genres = person["pref_movie"].split("|")
        for genre in genres:
            if genre in film_counts:
                film_counts[genre] += 1
            else:
                film_counts[genre] = 1
    else:
        genre = person["pref_movie"]
        if genre in film_counts:
            film_counts[genre] += 1
        else:
            film_counts[genre] = 1
            
most_popular_genre = max(film_counts, key=film_counts.get)

print(most_popular_genre)   
    

################################################################################

print(colored("Genres de film par ordre de popularité :", 'yellow'))
sorted_genre = sorted(film_counts, key=film_counts.get, reverse=True)

print(sorted_genre)

################################################################################

print(colored("Liste des genres de film et nombre de personnes qui les préfèrent :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Age moyen des hommes qui aiment les films noirs :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Age moyen des femmes qui aiment les drames et habitent sur le fuseau horaire, de Paris : ", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("""Homme qui cherche un homme et habite le plus proche d'un homme qui a au moins une
préférence de film en commun (afficher les deux et la distance entre les deux):""", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des couples femmes / hommes qui ont les même préférences de films :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('MATCH' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
"""
    On match les gens avec ce qu'ils cherchent (homme ou femme).
    On prend en priorité ceux qui ont le plus de gouts en commun.
    Puis ceux qui sont les plus proches.
    Les gens qui travaillent chez google ne peuvent qu'être en couple entre eux.
    Quelqu'un qui n'aime pas les Drama ne peux pas être en couple avec quelqu'un qui les aime.
    Quelqu'un qui aime les films d'aventure doit forcement être en couple avec quelqu'un qui aime aussi 
    les films d'aventure.
    La différences d'age dans un couple doit être inférieure à 25% (de l'age du plus agé des deux)
    ߷    ߷    ߷    Créer le plus de couples possibles.                  ߷    ߷    ߷    
    ߷    ߷    ߷    Mesurez le temps de calcul de votre fonction         ߷    ߷    ߷    
    ߷    ߷    ߷    Essayez de réduire le temps de calcul au maximum     ߷    ߷    ߷    

"""
print(colored("liste de couples à matcher (nom et id pour chaque membre du couple) :", 'yellow'))
print(colored('Exemple :', 'green'))
print(colored('1 Alice A.\t2 Bob B.'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))
