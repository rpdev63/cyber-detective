# Cyber Détective

## PARTIE 1 - WEB SCRAPPING 

Un scrapper récupère les infos sur les livres du site https://books.toscrape.com/ , insère les données dans une BDD MariaDB, et créé un fichier books.csv

#### Procédure pour démarrer le scrapper

1 ) Lancer bash depuis le répertoire race Cyber-detective/

```
python -m venv env
source env/Scripts/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
  

2 ) Remplir le fichier .env à la racine du projet, renseigner votre nom d'utilisateur et mot de passe mariaDb, ainsi que le numéro de port ( par défaut : 3306 ou 3307 si vous avez WAMP et PhpMyAdmin )
⚠️ *PhpMyAdmin doit être installé et opérationnel pour cette étape, si vous ne l'avez pas déjà fait télécharger WAMP [ici](https://www.wampserver.com/)*


3 ) Démarrer l'application / le scrapper
```
python -run.py
```

## PARTIE 2 - ANALYSE DE TWEETS

Ce notebook permet l'analyse de tweets concernant des livres célèbres qui ont été commentés. 
L'extraction des tweets n'a pas été faite par l'API, les csv ont été directement fournis.

#### Procédure pour démarrer le notebook

1 ) Importer les données depuis [le drive](https://drive.google.com/drive/folders/1JVQ83p1c4PQpGrMWYoHkIt6lXI_pe2Co) et coller le contenu dans le dossier /data

2 ) Lancer le notebook Analyse_tweets.ipynb qui se trouve dans le dossier /notebooks. Utiliser jupyter note book depuis anaconda ( [installer anaconda](https://www.anaconda.com/products/distribution) ) ou installer/lancer jupyter notebook
```
python3 -m pip install --upgrade pip
pip install notebook
python -m notebook .
```

3 ) Corriger les erreurs dans les csv indiquées en exécutant le début du notebook, il y a 4/5 lignes à supprimer / modifier...

![img notebook][img]

[img]: notebooks/parseerror.PNG "Logo Title Text 2"

Installer les librairies python manquantes si nécessaire.
