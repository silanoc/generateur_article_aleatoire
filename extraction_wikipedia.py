#! /usr/bin/env python3
# coding: utf-8

import wikipedia

"""Générer avec l'aide de chat-GPT"""

# Définir la langue
wikipedia.set_lang("fr")  

# Définir le nombre d'articles à extraire
num_articles = 1

# Obtenir une liste aléatoire de titres d'articles
titles = wikipedia.random(num_articles)

# Pour chaque article, extraire le contenu et enregistrer dans un fichier
for title in titles:
    # Obtenir le contenu de l'article
    content = wikipedia.page(title).content
    
    # Supprimer les signes == ou === et double saut de ligne du contenu
    content = content.replace("===", "")
    content = content.replace("==", "")
    content = content.replace("\n\n", "")
        
    # Créer un fichier avec le titre de l'article comme nom
    file_name = "./vrai_texte/wikipedia/"  + title + ".txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)