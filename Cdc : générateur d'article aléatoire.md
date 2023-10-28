# Cdc : générateur d'article aléatoire
auteur : Gabriel-le
création : 1 novembre 2021
refonte : 2023-10/28

## Contexte 
- C'est un projet perso pour m'améliorer, écrire un cahier des charges et écrire un programme avec du hasard dans un esprit de traitement du langage.
- Premier CDC pour un code perso. Il est mélangé au cahier des spécificités techniques. Car je ne suis pas encore à l'aise pour séparer, plus simple..., 
- Projet perso mono personne et sert à structurer ma pensée avant de coder

## Objectifs : 
- On donne plein d'articles sur un sujet (exemple affaire Bigmalion) et on génère un article aléatoire.
- Effet attendu, texte +- cohérent si les sources sont proches ou pas. L'effet peut être étonnant si on mélange politique, sciences...

## Périmètre : 
- Pour moi. 
- Pour présenter le code à d'autres.
- En version améliorée pour d'autres utilisataires.

## Intelligence du système :
- nulle à faible. Il s'agit uniquement de probabilité. Après un mot il y a 50 % d'un autre, 25% d'un autres deuxième et 25% d'une troisième ...
- améliorations avec grammaire, gestion noms propres...

## Architecture :
- Un dossier pour mettre tous les articles à analyser : 'vrai_texte'
- Un dossier pour les textes générés 'textes_generes'
    - [x] Textes de sortie : horodatage+".txt" pour éviter même nom
- un dossier avec les fichiers avec les fréquences des mots suivants (json (?) )
- Affichage :
    - ~~console~~
    - ~~interface graphique~~
    - jupyter notebook
        - brut
        - avec des widgets
- ~~architecture MVC https://fr.m.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur~~
## fichiers de code python,
~~- Modèle vue contrôle~~
~~- Modèle.py~~
~~- Vue graphique.py~~
~~- Contrôle console.py~~
~~- Contrôle graphique.py~~
~~- Logiciel console.py~~
~~- Logiciel graphique.py~~
- generateur_article.ipynb

## Ressources, cours openclasseroom
- https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4463200-organisez-un-script
    - Tous les fichiers possèdent un main init
    - Utf8
- bibliothèque perso ?
- Test unitaires et co

## Spécificités
### Entrée
- [x] nombre de fichier au choix.
- Format d'entrée :
    - [x] .txt
    - [ ] autre ?
#### User story
L'utilisataires doit pouvoir ajouter des textes de différentes sources :
- [x] Via wikipédia
- [ ] Via une URL standard, plusieurs url
- [x] via des fichiers txt déposé directemlent dans dossier "vrai_texte"
A partir pdf, Doc....
### Sortie
- [x] Écran (dans notebook)
- [x] Fichier .txt (dans 'textes_generes')
- Faire un ou plusieurs textes
### Gestion de la ponctuation
- Version test : non gérée, la supprimer
- Version améliorée : prise en compte
### Texte généré
- Quel est le premier mot ? Hasard, les plus fréquents
- Taille ? Hasard, moyenne, le plus grand, le plus petit ? -> besoin de le mesurer stocker
### vérifiabilité 
- l'analyse doit pouvoir dire à partir de quel(s) texte ça a été produit
- le texte généré doit pouvoir dire quelle base a été utilisé 
### programmation objet
- Chaque texte analysé est un objet,
- L'analyse est un objet 
- Chaque texte généré est un objet
## Fonctions
- Analyser un texte et le mettre dans un fichier 
- Analyser une collection et le mettre dans un fichier 
- Ouvrir, compléter, sauver une analyse, 
- Génerer à partir d'une analyse
- Générer à partir d'une collection
- expoter les résultats
## Ordre de développement
- Analyser et générer un texte
- Interface minimale dans une console
- Exporter texte
- Générer/exporter plusieurs textes
- Analyser plusieurs textes
## Versions ultérieures
- Web ou application
- textes en entré à partir d'url
