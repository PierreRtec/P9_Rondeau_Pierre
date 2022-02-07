# Application web Django dédié aux critiques de livres et d'articles
---
# Prérequis

## Git Clone repository

> git clone https://github.com/PierreRtech/P9_Rondeau_Pierre

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



## I - User Interface

### Page d'accueil :

http://127.0.0.1:8000/awebapp/homepage/

### Page d'inscription :

http://127.0.0.1:8000/awebapp/signup/

### Page de connexion / déconnexion :

http://127.0.0.1:8000/awebapp/login/

http://127.0.0.1:8000/awebapp/logout/

### *connexion requise* Page du flux d'actualité :

http://127.0.0.1:8000/awebapp/flux/

### *connexion requise* Page des abonnements :

http://127.0.0.1:8000/awebapp/abos/

### *connexion requise* Mes posts :

http://127.0.0.1:8000/awebapp/posts/

### *connexion requise* Demandes de critiques de livre / article :

http://127.0.0.1:8000/awebapp/create-ticket/


### *connexion requise* Création de critiques (avec ou sans réponse à une demande) :

http://127.0.0.1:8000/awebapp/create-review/

## II - Utilisation avancée

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

#### Création d'un super-utilisateur

documentation Django : https://docs.djangoproject.com/fr/1.8/intro/tutorial02/

> python manage.py createsuperuser

..identifiants
..mdp
..mdp confirmation
..success !

> py -m manage runserver

rendez-vous sur http://127.0.0.1:8000/admin

entrez vos identifiants et accèdez à l'espace administrateur de votre application web
