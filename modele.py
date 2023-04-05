#! /usr/bin/env python3
# coding: utf-8

"""
modéle
pour console et fenetre graphique

Warning : attention aux espaces
"""

import random

from texts_de_test import *
from dico_de_test import *

#AFAIRE : reprendre le code de chercher les mots avec split ???

class articlepresse():
    """chaque article qui servira d'entrée en apprentissage sera mis dans un objet pour analyse, extraction..."""
    
    def __init__(self, text):
        """initilisation
        arg: 
            une chaine de texte (si possible longue)
        return :
            aucun
        """
        self.texte:str = text #le texte sur lequel on travail
        self.dicostatique:dict = {} #pour la fonction liste_et_compte_mots
        self.dicodoublons:dict = {} #pour la fonction cherche_binomes_mots - ce qui est recherché
    
    def retirer_ponctuation(self, txt_a_nettoyer:str) -> str:
        """ La première version du logiciel est sommaire. Pour se simplifier la vie, il faut supprimer tous les signe de ponctuations.
        
        arg:
            une chaine de texte avec de la ponctuation
        return:
            une chaine de texte sans ponctuation
        """
        ponctuation:list = [",",";",":","!","?",".","/","«","»",'"',"–","(",")"]
        for signe in ponctuation:
            txt_a_nettoyer = txt_a_nettoyer.replace(signe, "")
        #mettre un espace entre les mots avec apostrophe afin de bien les séparer
        apostrophe = ["’","'"]
        for apost in apostrophe:
            txt_a_nettoyer = txt_a_nettoyer.replace(apost, " ")
        #quand on supprime un : par exemple, cela fait deux espace. Remplacer ces artefacts de cagage
        for _ in range(len(self.texte)):
            txt_a_nettoyer = txt_a_nettoyer.replace("  ", " ")
        for _ in range(len(self.texte)):
            txt_a_nettoyer = txt_a_nettoyer.replace(" ", " ")
        return txt_a_nettoyer

    def liste_et_compte_mots(self, texte_a_traiter:str) -> list[list,dict]:
        """Compte le nombre d'occurence d'un mot.
        Fonction créée un peu par erreur, mais elle peut être utile pour faire des statistiques.
        arg : 
            texte_a_traiter (str)
        return : 
            2 object dans un liste. La liste des mots de la chaine et le comptrage de chaque mot dans un dictionnaire
            """
        liste_mot: list[str] = texte_a_traiter.split(" ")
        dicostatistique = {}
        for mot in liste_mot:
            if mot in dicostatistique:
                dicostatistique[mot] += 1
            else:
                dicostatistique[mot] = 1
        return [liste_mot, dicostatistique]
    
    def cherche_binomes_mots(self, texte_a_traiter:str) -> dict:
        """la fonction principale de l'objet : faire un dictionnaire de fréquences des mots qui se suivent.
        
        arg :
            self
        return :
            dictionnaire {mot1:[mot2, mot3, mot3, mot4],...}
        """
        liste_mots_suivant:list = []
        dicodoublons:dict = {}
        #recherche des espaces délimitants les mots
        list_position_espace = []
        for i in range(len(texte_a_traiter)):
            if texte_a_traiter[i] == " ":
                list_position_espace.append(i)
        #print(list_position_espace)
        #recherche doublons mot
        debut1 = 0
        for i in range(len(list_position_espace)-2): #AFAIRE : ATTENTION ça ne prends pas les deux derniers mot. A vérifier.
            fin1 = list_position_espace[i]
            fin2 = list_position_espace[i + 1]
            #print(debut1, fin1,fin2)
            mot1 = texte_a_traiter[debut1:fin1]
            mot2 = texte_a_traiter[fin1:fin2]
            debut1 = list_position_espace[i]
            #print(mot1,mot2)
            liste_mots_suivant.append([mot1, mot2])
        #print(liste_mots_suivant)
        #fait un dictionnaire avec toutes les occurences possible après un même mot.
        #les doublons sont normaux, cela veut dire que le mot revient plusieurs fois, cela correspond au calcul de leur fréquence   
        for j in range(len(liste_mots_suivant)):
            if liste_mots_suivant[j][0] in dicodoublons.keys():
                #print('doublons')
                dicodoublons[liste_mots_suivant[j][0]].append(liste_mots_suivant[j][1])
            else:
                #print('nouveau')
                dicodoublons[liste_mots_suivant[j][0]]=[(liste_mots_suivant[j][1])]
        # Warning : il y a des espace en trop (tenu en compte pour le reste et tests)
        return dicodoublons 
    
    def tout_enchainer(self) -> None :
        self.texte = self.retirer_ponctuation(self.texte)
        #self.dicostatique = self.liste_et_compte_mots(self.texte)[1]
        #print(self.dicostatique)
        #print("--------------")
        self.dicodoublons = self.cherche_binomes_mots(self.texte)
        

class articleauhasard():
    """génére un texte aléatoire à partir d'un dictionnaire
    
        arg :
            dictionnaire {mot1:[mot2, mot3, mot3, mot4],...}
            typiquement le dictionnaire généré par le return de cherche_binomes_mots(), ou d'une sauvegarde issus de cette fonction.
        
        return
            une chaine de texte avec les mots du dictionnaire dans un ordre aléatoire.
            elle pourra aller dans un doc txt pour sauvegarde
    """

    def __init__(self, mondico:dict):
        """initilisation
        
            arg: 
                une chaine de texte (si possible longue)
        """
        self.mondico: dict = mondico #le dictionnaire sur lequel on travail
        self.textealeatoire : str ="" #le texte que l'on veut
    
    def choixmotpourcommencer(self, dico: dict)-> str:
        """a utiliser pour le premier mot, mais aussi si un mot ne peut pas en trouver d'autre, faire une proposition pour eviter une erreur et continuer """
        #Mettre les clefs dans une liste
        liste_des_mots : list = []
        for key in dico:
            liste_des_mots.append(key)
        #choix lui meme
        mot: str = liste_des_mots[random.randint(0, len(liste_des_mots))]
        #retirer l'espace s'il existe
        if mot[0] == " ":
            mot = mot[1:]
        return mot      

    def chercherlemotsuivant(self, dico: dict, mot: str) -> str:
        """à partir d'un mot, sortir aléatoire un mot dans ceux pouvant le suivre stocké dans le dictionnaire"""
        liste_des_possible: list = dico[" " + mot] #WARNING on remet un espace car dans la version du moment, il y a un espace dans le dico et c'est pas bien
        mot: str = liste_des_possible[random.randint(0, len(liste_des_possible) -1 )]
        #retirer l'espace s'il existe
        if mot[0] == " ":
            mot = mot[1:]
        return mot      
    
    def genereruntexte(self, taille_article: int) -> None:
        """intier avec choixmotpourcommencer(), puis enchainer chercherlemotsuivant()
        taille_article est le nombre de mot que l'on veut pour l'article aléatoire"""
        mot: str = self.choixmotpourcommencer(self.mondico)
        self.textealeatoire += mot
        for _ in range(taille_article - 1):
            new_mot: str = self.chercherlemotsuivant(self.mondico, mot)
            mot = new_mot
            self.textealeatoire = self.textealeatoire + " " + mot
            
def addition_dico(grand_dico : dict, petit_dico : dict)-> dict:
    for keys, values in petit_dico.items():
        if keys in grand_dico:
            liste_intermediaire = grand_dico[keys]
            for item in values:
                liste_intermediaire.append(item)
            grand_dico[keys] = liste_intermediaire
        else:
            grand_dico[keys] = values
    return grand_dico
 
def main():
    #a = articlepresse(textetest2)
    #a.tout_enchainer()
    #print(a.dicodoublons)
    

    b = articleauhasard(dicotest2)
    b.genereruntexte(30)
    print(b.textealeatoire)
    

if __name__ == "__main__":
    main()