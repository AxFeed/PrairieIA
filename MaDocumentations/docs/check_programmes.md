# Vérification des programmes installés

## Fonction : `Check_Programmes($NomProgramme)`

Cette fonction vérifie si un programme est installé sur l’ordinateur.

## Paramètres

- `$NomProgramme` : Le nom du programme à vérifier (ex : "Google Chrome").

## Fonctionnement

1. Cherche le programme dans le registre Windows :
   - `HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*`
   - `HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*`
   - `HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*`
2. Si le programme est trouvé, retourne un message confirmant l’installation.
3. Si le programme n’est pas trouvé, propose un lien pour l’installer (pour Chrome, Firefox, Brave, Node, Python).
4. Si le programme n’est pas reconnu, affiche un message générique.

## Exemples

- Check_Programmes("Google Chrome")
- Check_Programme("Brave")
