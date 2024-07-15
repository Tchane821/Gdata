# Scripts pour Guillaume : conversion, filtre et analyse

---

## A. Installation de l'environnement de travail :

1) Installer VsCode (https://code.visualstudio.com/download).
2) Ouvrir le dossier du projet avec VSCode.
    1) Clique droite sur le dossier.
    2) Ouvrir avec VsCode.
3) Dans VsCode ouvrir un terminal.
    1) Dans l'onglet *View* en haut.
    2) Sélectionner *Terminal*.
    3) Il s'affiche en bas de VsCode
    4) Cliquer dedans pour commencer à taper les commandes.
4) Taper la commande ```python --version``` pour connaitre la version de Python et donc savoir s'il est installé.
    1) Si c'est le cas, alors il doit répondre la version de Python.
    2) Sinon, il faut installer Python (https://www.python.org/downloads/).
5) Taper la commande ```pip --version``` pour savoir si *pip* est installé.
    1) Si oui, il répond sa version.
    2) Sinon, il faut l'installer en tapant cette commande ```python get-pip.py```.
6) Maintenant, on va installer les modules nécessaires aux scripts.
    1) Pour installer pandas et *matplotlib*, il faut lancer les commandes suivantes :
    2) ```pip install pandas```
    3) ```pip install matplotlib```
7) On va maintenant créer les dossiers nécessaires aux fonctionnements des scriptes. S'ils ne sont pas déjà créés, alors
   créé les dossiers :
    1) *csv* manuellement ou en tapant la commande ```mkdir csv```.
    2) *data* manuellement ou en tapant la commande ```mkdir data```.
    3) *graph* manuellement ou en tapant la commande ```mkdir graph```.

---

## B. Utilisation des scripts :

### B.a. Convertir CXP en CSV :

Le scrypt **converter.py** permet de transformer tous les fichiers qui se trouvent dans le dossier **data**,
en CSV dans le dossier **csv**.  
Pour l'exécuter, taper la commande ```python converter.py```.

- Ce script est nécessaire avant de lancer les autres.
- Ne mettre que des fichiers CXP dans le dossier data.

### B.b. Analyse graphique :

Le script **analyzer_plot.py** permet de générer des graphiques à partir des fichiers CSV.  
Ces graphiques sont sauvegardés dans le dossier **graph**.  
Pour l'exécuter, taper la commande ```python analyzer_plot.py```.

### B.c. Analyse chiffrée :

Le script **analyzer_stats** permet de créer un fichier CSV de résultats contenant les valeurs calculées pour tous les
fichiers data.  
Pour l'exécuter, taper la commande ```python analyzer_stats.py```.

Les colonnes du fichier **result.csv** correspondent à :

- NB_SAMPLE : Nombre d'enregistrements fait par la machine.
- AGE : Age du patient.
- ID : Identifiant du patient.
- EXE : Nom de l'exercice réalisait par le patient.
- SEX : Sex du patient.
- WEIGHT : Poids du patient.
- HEIGHT : Taille du patient.
- NBTTG : Nombre total d'enregistrement conservé après les filtres.
- NBTTFLE : Nombre total d'enregistrement en flexion après les filtres.
- NBTTEXT : Nombre total d'enregistrements en extension après les filtres.
- NBISOFLE : Nombre total d'enregistrements en flexions et en iso après les filtres.
- NBISOEXT : Nombre total d'enregistrements en extensions et en iso après les filtres.

---

## C. Au cœur des scripts :

Les scripts ainsi écrits sont censés être lisibles et pas trop complexes (c'est tout relatif).  
Je vais tenter de le rendre plus lisible en ajoutant des commentaires afin que tu puisses comprendre et potentiellement
modifier ce code plus tard.  
Note à toi, crée-toi un compte github (https://github.com/signup) et envoie-moi l'e-mail que tu as utilisé pour ça.