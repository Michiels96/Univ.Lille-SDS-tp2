# TP: Etude d'un programme vulnérable en Python (Application Web)

Au cours de ce TP, vous allez étudier une application web minimaliste, qui est vulnérable à une faille d'injection SQL. 

Les prérequis sont:
 * Une machine sous Linux avec Python 3
 * Accès à un serveur MySQL (sur votre machine, ou ailleurs, peu importe)
 * Savoir programmer en Python
 * Connaitre les bases de l'HTML, du javascript, et du SQL
 * Avoir vu le cours sur les injections SQL

Vous pouvez utiliser votre machine OpenStack, comme dans le dernier sujet sur les permissions Unix.
Vous pouvez aussi utiliser l'image OVA disponible sur: https://nextcloud.univ-lille.fr/index.php/s/BMawwN5m8AcT9oJ

## Préparation 

Si vous avez suivi le module ISI, la préparation est la même jusqu'a la
partie "création de la table MySQL" donc vous pouvez réutiliser ce que vous
avez déja fait.

Dans ce dépôt, vouz trouverez le fichier `serveur.py` contenant le source python du serveur vulnérable.

### Préparation d'un environnement virtuel Python3

Un environnement virtuel Python3 est une sorte d'installation indépendante et auto-suffisante de Python3, qui sera placée dans votre dossier personnel, et dans laquelle vous pouvez installer des modules Python3 sans avoir besoin des droits root, ni de toucher au reste du système.

Si vous travaillez avec votre propre machine, assurez vous d'abord d'avoir installé l'outil de création d'environnement virtuel (sous Ubuntu/Debian: `sudo  apt install python3-venv`)

Ensuite, préparez l'environnement virtuel avec la commande suivante (où `<nom de dossier>` est à remplacer par le nom du dossier qui contiendra votre environnement virtuel)

```
python3 -m venv <nom de dossier>
```

Par exemple: `python3 -m venv monEnvTP`

### Activation de l'environnement virtuel

Pour travailler avec l'environnement virtuel que vous venez de préparer, vous devez d'abord l'activer avec la commande suivante:

```
source <chemin vers votre environnement virtuel>/bin/activate
```

Par exemple: `source monEnvTP/bin/activate`

Cette activation ne persiste que pendant la session shell/terminal en cours, et devra être refaite si vous vous deconnectez, ou relancez un terminal. Pour savoir si l'environnement virtuel est activé, vous pouvez vérifier que son nom apparait, entre parenthèses, dans votre invite de commande shell. 

A partir de maintenant, toute les étapes à réaliser dans ce TP (y compris la suite des étapes de préparation) nécessitent que l'environnement virtuel soit activé.

### Installation des modules Python3 nécessaires

Installez les modules nécessaires dans votre environnement (n'oubliez pas qu'il doit être activé) en tapant les commandes suivantes:

```
pip3 install cherrypy
pip3 install mysql-connector-python
```

Le module `cherrypy` est un framework d'applications Web en python, le module `mysql-connector-python` permet de se connecter à une base MySQL.

### Création de la table MySQL

Pour créer la table qui servira à l'application, faire:

```
mysql -p -u <votre user> <votre base> < contenu-base.sql
```

### Configuration de l'accès à la base de données

Renommez (ou copiez) le fichier de configuration de base de données `config.py.sample` en `config.py` et éditez le pour y mettre les informations d'accès à votre base MySQL.

Etant donné que le fichier `config.py` contient le mot de passe de votre serveur MySQL, vous prendez garde à ne pas le commit sur votre dépôt git (vous pouvez, par exemple, l'ajouter au `.gitignore`).

## Travail à réaliser

### Se familiariser avec l'application

Lancez l'application avec la commande suivante (en étant dans le dossier du dépôt git, et avec l'environnement virtuel activé):

```
./serveur.py
```

Les erreurs les plus fréquentes que vous pouvez rencontrer lors du lancement de du serveur sont:
 * Fichier `serveur.py` introuvable: vérifiez que vous êtes bien positionné dans le dossier du dépot git.
 * Modules introuvables (cherrypy ou mysql connector): assurez vous d'avoir activé l'environnement virtuel
 * Problème de connexion à la base de données: Vérifiez que les informations fournies dans `config.py` sont exactes
 * Port 8080 occupé: vérifiez que vous n'avez pas un autre serveur qui écoute sur le port 8080 (potentiellement une autre instance de `serveur.py` lancée sur un autre terminal)

Si cela fonctionne, vous aurez une ligne du type:
```
[03/Dec/2020:13:10:03] ENGINE Serving on http://127.0.0.1:8080
```

Vous devrez garder ce terminal ouvert pendant toute l'utilisation du serveur. Pour le stopper, faites un Ctrl-C dans le terminal où vous l'avez lancé.

## Partie 1

La première partie se déroule sur la page /view de l'application

Cette page permet d'entrer l'ID d'un article et d'afficher
le texte correspondant, ceci est stocké dans la table `articles` de la base
de données.

### Exploiter la vulnérabilité pour récuperer des données

En utilisant la méthode vue en cours, exploitez la faille d'injection SQL
pour récuperer l'ensemble des données présente dans la table `private`


## Partie 2

La première partie se déroule sur la page /login de l'application

Cette page présente une authentification, les login et password sont stockés
dans la table `users` de la base de données.


### Exploiter la vulnérabilité pour contourner l'authentification

En utilisant la méthode vue en cours, exploitez la faille d'injection SQL
pour contourner l'authentification

### Exploiter la vulnérabilité pour récuperer des mots de passes

En utilisant la méthode vue en cours, exploitez la faille d'injection SQL
pour récuperer le mot de passe de l'utilisateur `admin` 


### Exploiter la vulnérabilité pour récuperer des données

En utilisant la méthode vue en cours, exploitez la faille d'injection SQL
pour récuperer l'ensemble des données présente dans la table `private`
