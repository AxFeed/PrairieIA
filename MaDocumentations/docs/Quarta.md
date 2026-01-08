# Documentation du code de composeur de groupe

Ce code permet de composer des groupes random de X personne(s) en fonction d'une variable nombre par groupe qu'on lui envoi

Il utilise une fonction principale : `OrganisateurDeGroupe`.

[Lien vers le GIT](https://github.com/AxFeed/PrairieIA/blob/main/Composition%20de%20groupe/Createur_de_groupe.py)


## Composeur de groupe

### Fonction : `OrganisateurDeGroupe(nombreParGroupe)`

Cette fonction retourne X groupe de N personne, N étant la variavke nombreParGroupe.

### Paramètres

- `$nombreParGroupe` : Le nombre de personne par groupe (ex : "3").

### Fonctionnement

1. Boucle tant que la liste des personnes n'est pas vide
2. Tire un nombre random entre 0 et le nombre de personne dans la liste, nombre random qui sera l'index de la personne de notre tableau de personne
3. Ajoute la personne dans un nouveau tableau, puis l'enléve du tableau des personnes
4. Si, la taille du groupe de personne est égale au nombre de personne qu'on veut par groupe, alors on l'ajoute à notre tableau de groupe, puis on le réinitialise
5. Si, notre liste de personne est vide, alors on ajoute quand même notre groupe de personne au tableau de groupe

### Exemples

- ```py OrganisateurDeGroupe(3)``` 
```
Dans mon tableau 1 j'ai
Asma
Yacine
Khrisly
Dans mon tableau 2 j'ai
Ludovic
Lilian
Inès
Dans mon tableau 3 j'ai
Noemie
Manon
Ahmadola
Dans mon tableau 4 j'ai
Manar
Danitza
```
- ```py OrganisateurDeGroupe(5)```
```
Dans mon tableau 1 j'ai
Yacine
Manon
Asma
Manar
Danitza
Dans mon tableau 2 j'ai
Lilian
Inès
Noemie
Ahmadola
Khrisly
Dans mon tableau 3 j'ai
Ludovic
```