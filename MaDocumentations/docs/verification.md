#Documentation du Script PowerShell

Ce script permet de :

- Vérifier si certains programmes sont installés sur un ordinateur Windows.
- Vérifier des calculs simples (addition de deux nombres).

Il utilise deux fonctions principales : `Check_Programmes` et `Check_Calcul`.

[Lien vers le GIT](https://github.com/AxFeed/PrairieIA/blob/main/Script%20Powershell/Verification.ps1)


#Vérification des programmes installés

##Fonction : `Check_Programmes($NomProgramme)`

Cette fonction vérifie si un programme est installé sur l’ordinateur.

##Paramètres

- `$NomProgramme` : Le nom du programme à vérifier (ex : "Google Chrome").

##Fonctionnement

1. Cherche le programme dans le registre Windows :
   - `HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*`
   - `HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*`
   - `HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*`
2. Si le programme est trouvé, retourne un message confirmant l’installation.
3. Si le programme n’est pas trouvé, propose un lien pour l’installer (pour Chrome, Firefox, Brave, Node, Python).
4. Si le programme n’est pas reconnu, affiche un message générique.

##Exemples

- ```py Check_Programmes("Google Chrome")``` # Google Chrome est bien installe sur l'ordinateur !
- ```py Check_Programme("Bidule")``` # Bidule n'est PAS installe sur l'ordinateur ! Mais vous pouvez l'installer ici...

#Vérification des calculs

##Fonction : `Check_Calcul($a, $b)`

Cette fonction vérifie si la somme de deux nombres est égale à 4.

##Paramètres

- `$a` : Premier nombre
- `$b` : Deuxième nombre

##Fonctionnement

- Affiche un message pour indiquer le résultat de l’addition.
- Retourne un message :
  - Si `$a + $b = 4` → `"a + b est bien egal a 4"`
  - Sinon → `"a + b n'est pas egal a 4"`

##Exemples
- ```py Check_Calcul 2 2```   # Retourne : "2 + 2 est bien egal a 4"
- ```py Check_Calcul 2 3```  # Retourne : "2 + 3 n'est pas egal a 4"

