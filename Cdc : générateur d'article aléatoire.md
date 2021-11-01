# Cdc : générateur d'article aléatoire
auteur : Gabriel-le
création : 1 nobembre 2021

## Contexte 
- C'est un projet perso pour m'améliorer , écrire un cahier des charge et écrire un programme avec du hasard dans un esprit de traitement du langage.
- Premier CDC pour un code perso. Il est  mélangé au cahier des spécificités techniques. Car pas encore à l'aise pour séparer, plus simple..., Projet perso mono personne et sert a structurer ma penser avant de coder

## Objectifs : 
- On donne pleins d'articles sur un sujet (exemple affaire bigmalion) et on génère un article aléatoire.
Effet attendu, texte +- cohérent selon si les sources sont proches ou pas. L'effet peut être étonnant si on mélange politique, sciences...

## Périmètre : 
- Pour moi. 
- Pour présenter le code à d'autres.
- En version améliorée pour d'autre utilisataires.

## Intelligence du système :
- nulle a faible. Il s'agit uniquement de probabilité. Après un mot il y a 50 % d'un autre, 25% d'un autres ...
- améliorations avec grammaire, gestion nom propres...


## Architecture :
- Un dossier pour mettre tous les articles à analyser
- Un dossier pour les textes générés
    - Textes de sortie : horodatage+"txt_genere.txt" pour éviter même nom
- un dossier avec les fichier avec les fréquences des mots suivants (json (?) )
- Affichage :
    - console
    - interface graphique
- architecture MVC https://fr.m.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur
### fichiers de code python, 
- Modèle vue contrôle
- Modèle.py
- Vue graphique.py
- Contrôle console.py
- Contrôle graphique.py
- Logiciel console.py
- Logiciel graphique.py

## Ressources, cours openclasseroom
- nom du cours
    - Tous possède un main init
    - Utf8
- bibliothèque perso ?
- Test unitaires et co

## spécificités
### Entrée
- 1 txt
- Plusieurs txt
- Format d'entrée : txt, autre ?
### Sortie
- Écran
- Fichier txt PDF
- Faire un ou plusieur textes
### Gestion de la ponctuation
Version test : non géré, la supprimer
Version améliorée : prise en compte
### Texte généré
- Quel est le premier mot ? Hasard, les plus fréquent
- Taille ? Hasard, moyenne, le plus grand, le plus petit ? -> besoin de le mesurer stocker
### vérificabilité 
- l'analayse doit pouvoir dire à partuir de quel(s) texte ça a été produit
- le texte généré doit pouvoir dire quelle base a été utilisé 
### programmation objet
- Chaque texte analysé est un objet,
- L'analyse est un objet 
- Chaque texte généré est un objet
## Fonctions
- Analyser un texte et le mettre dans un fichier 
- Analyser une collection et le mettre dans un fichier 
- Ouvrir, compléter, sauver une analyse, 
- Génere à partir d'une analyse
- Générer à partir d'une collection
- exporet les résultats
## Ordre de développement
- Analyser et générer un texte
- Interface minimale console
- Exporter texte
- Générer/exporter plusieurs textes
- Analyser plusieurs textes
## Versions ultérieures
- Web ou application
- textes en entré à partir d'url