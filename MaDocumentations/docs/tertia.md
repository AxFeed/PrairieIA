# Réponses à l'exercice 3

Voici une requête Http => GET https://dummyjson.com:443/recipes?limit=10 HTTP/2, on va expliquer pas à pas son fonctionnement

##C’est quoi une requête HTTP ?

Une requête HTTP c'est un message envoyé par l'ordinateur pour demander des informations à un serveur

##C’est quoi un DNS ?

Un DNS c'est un nom de domaine pour aller sur une adresse sur Internet, un peu comme un annuaire téléphonique

##C’est quoi GET ?

GET c'est une méthode en HTTP pour interroger le serveur

##C’est quoi https:// ?

C'est pour avoir la version sécurisé du http où les données sont chiffrées

##C’est quoi dummyjson.com ?

Dummyjson c'est le domaine (serveur) auquel on s'adresse

##C’est quoi 443 ?

443 est le port sur lequel on se connecte sur ce serveur

##C’est quoi recipes ?

Recipe c'est l'endpoint de l'API sur lequel on va chercher les informations

##C’est quoi ? ?

Le ? est utilisé ici afin de faire une query (demande) au serveur afin d'interroger sa base de donnée

##C’est quoi limit ?

Limit c'est une demande pour limité les données que le serveur va nous renvoyer pour n'avoir que les X premières lignes de la base de données

##C’est quoi 10 ?

Comme dit au dessus c'est que pour le serveur ne nous renvoi que les 10 premières lignes

##C’est quoi HTTP/2 ?

C’est une version du protocole HTTP plus rapide et efficace que HTTP/1.1

##Que contient la réponse à cette requête ?

La réponse à cette requête donnera les 10 premières recettes de la base de données de dummyjson.com