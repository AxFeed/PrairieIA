import random

apprenantsList = ["Inès", "Asma", "Khrisly", "Yacine", "Ludovic", "Manon", "Lilian", "Manar", "Ahmadola", "Noemie", "Danitza"] # Ma liste d'apprenant
tableauxApprenant = [] # Ma liste qui va contenir les différents tableaux d'apprenants
tableau = [] # La liste qui contiendra un tableau que je mettrai dans la liste de tableau

def OrganisateurDeGroupe(nombreParGroupe):
    i = 0
    while len(apprenantsList) != 0: # Je boucle tant que j'ai des apprenants dans la liste
        rnd = random.randint(0, len(apprenantsList)-1) # Je tire un nombre random entre 0 et la longueur de ma liste
        tableau.append(apprenantsList[rnd]) # J'ajoute l'apprenand X à mon tableau
        apprenantsList.pop(rnd) # Je supprime l'apprenant de la liste pour qu'il ne soit plus présent
        i += 1
        
        if(i == nombreParGroupe): # Si j'arrive à ma limite alors j'ajoute une copie du tableau puis je le clear pour revenir à une liste vide
            tableauxApprenant.append(tableau.copy())
            tableau.clear()
            i = 0
            
    if len(tableau) != 0:
        tableauxApprenant.append(tableau)
    return tableauxApprenant

NombreApprenantParTab = int(input("Combien voulez vous d'apprenant par tableau ? "))
tableauxApprenant = OrganisateurDeGroupe(NombreApprenantParTab);
i = 1
for tabApprenant in tableauxApprenant:
    print("Dans mon tableau " +str(i) + " j'ai")
    for apprenant in tabApprenant:
        print(apprenant)
    i+= 1