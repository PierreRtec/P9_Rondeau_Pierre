# Application web Django dédié aux critiques de livres et d'articles
---
# Prérequis :

- Python 3.10
- Environnement virtuel
- pipenv

## Comment installer l'environnement virtuel ?
Dans votre terminal :

> pip install pipenv

> pipenv shell

> pipenv install

### Pour plus de précisions : https://pypi.org/project/pipenv/
---

## Comment lancer l'application "awebapp" ?
Dans votre terminal :

> cd ./src

> py -m manage runserver

Vous devriez voir apparaître dans votre terminale les lignes suivantes :

Day 25, 2049 - 10:00:00
Django version 4.0.1, using settings 'manage_site_P9.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Comme vous l'aurez compris, un Ctrl+C permettras de stopper le serveur.



## Pages & Fonctionnalités

### page 1 :


### page 2 :



### page 3 :


### page 4 :


### Générez un rapport flake8

+ pipenv install flake8
+ pipenv install flake8-html

créer un fichier qui s'appelle "setup.cfg"

mettre dedans : 

[flake8]
exclude =
	.git,
	env,
	__pycache__,
	ajout_liste_joueur.py,
	models/__pycache
	test.py

max-line-length = 119

#### COMMANDE création de rapport HTML >_

flake8 --format=html --htmldir=flake8-rapport

#### Dans votre terminal :

> black "nomdel'app"

Cela exécutera le module sur notre application. Si l'application s'appelait chessprogr alors ce serait "black chessprogr".

### Commandes utiles Django :

Si vous voulez mettre à jour la base de données sqlite3 vous pouvez la supprimée manuellement dans votre IDE.
Mais vous devrez refaire les migrations pour apporter les changements. 
Dans votre terminal assurez-vous de saisir :

> py -m manage makemigrations "nomdel'app"

No changes detected

> py -m manage migrate

Running migrations:
  Applying auth.[...]
  [...]
