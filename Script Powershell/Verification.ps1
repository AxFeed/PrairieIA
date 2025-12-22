function Check_Programmes($NomProgramme) {

    $paths = @(
        "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*",
        "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*",
        "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*"
    )

    $found = Get-ItemProperty $paths -ErrorAction SilentlyContinue |
             Where-Object { $_.DisplayName -like "*$NomProgramme*" }

    if ($found) {
        return "$NomProgramme est bien installe sur l'ordinateur !"
    } else {
		if($NomProgramme -eq "Google Chrome"){
        return "$NomProgramme n'est PAS installe sur l'ordinateur ! Mais vous pouvez l'installer ici : https://www.google.com/intl/fr_fr/chrome/"
		}elseif($NomProgramme -eq "Firefox"){
			return "$NomProgramme n'est PAS installe sur l'ordinateur ! Mais vous pouvez l'installer ici : https://www.firefox.com/fr/"
		}elseif($NomProgramme -eq "Brave"){
			return "$NomProgramme n'est PAS installe sur l'ordinateur ! Mais vous pouvez l'installer ici : https://brave.com/fr/"
		}elseif($NomProgramme -eq "Node"){
			return "$NomProgramme n'est PAS installe sur l'ordinateur ! Mais vous pouvez l'installer ici : https://nodejs.org/fr/download"
		}elseif($NomProgramme -eq "Python"){
			return "$NomProgramme n'est PAS installe sur l'ordinateur ! Mais vous pouvez l'installer ici : https://www.python.org/downloads/"
		}else{
			return "Il semblerai que ce programme ne soit aucun de ceux reconnus => $NomProgramme"
		}
    }
}

function Check_Calcul($a, $b) {
	Write-Output "`nVerifications des calculs...`n"
	if(($a+$b) -eq 4){
		return "$a + $b est bien egal a 4"
	}else{
		return "$a + $b n'est pas egal a 4"
	}
}

$programmes = @(
	"Google Chrome"
	"Firefox"
	"Brave"
	"Node"
	"Python"
	"Test pour erreur"
)

Write-Output "Verification des applications installees...`n"
if($programmes.lenght -ne 0){
	foreach($programme in $programmes){
		Check_Programmes("$programme")
	}
}else{
	Write-Output "Il semble que la liste d'applications soit vide !"
}

Check_Calcul 2 2
Check_Calcul 2 3

