#! /usr/bin/env python3
# coding: utf-8

"""
modéle
pour console et fenetre graphique
"""

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
        #Déclaration de varable 
        self.texte = text #le texte sur lequel on travail
        self.dicostatique = {} #pour la fonction liste_et_compte_mots
        self.dicodoublons = {} #pour la fonction cherche_binomes_mots - ce qui est recherché
    
    def retirer_ponctuation(self):
        """ La première version du logiciel est sommaire. Pour se simplifier la vie, il faut supprimer tous les signe de ponctuations.
        
        Il n'y a ni entrée (arg) ni sortie (return), c'est 'juste' une modification sur l'objet
        """
        ponctuation = [",",";",":","!","?",".","/","«","»",'"',"–","(",")"]
        for c in ponctuation:
            self.texte = self.texte.replace(c, "")
        #mettre un espace entre les mots avec apostrophe afin de bien les séparer
        apostrophe = ["’","'"]
        for d in apostrophe:
            self.texte = self.texte.replace(d, " ")
        #quand on supprime un : par exemple, cela fait deux espace. Remplacer ces artefacts de cagage
        for i in range(len(self.texte)):
            self.texte = self.texte.replace("  ", " ")

    
    def liste_et_compte_mots(self,texte_a_traiter):
        """Compte le nombre d'occurence d'un mot.
        Fonction créée un peu par erreur, mais elle peut être utile pour faire des statistiques.
        
        arg : 
            self
        return : 
            [liste[mot1,mot2,,...],dictionnaire {mot:nb,...}]
        #>>> liste_et_compte_mots("le petit chat de béatrice est sur le petit mur du jardin de Yves")
        #['le','petit','chat','de','béatrice','est','sur','le','petit','mur','du','jardin','de','Yves']
        #[['le','petit','chat','de','béatrice','est','sur','le','petit','mur','du','jardin','de','Yves'],{'le':2,'petit':2,'chat':1,'de':2,'béatrice':1,'est':1,'sur':1,'mur':1,'du':1,'jardin':1,'Yves':1}]
        """
        self.liste_mot = texte_a_traiter.split(" ")
        for mot in self.liste_mot:
            if mot in self.dicostatique:
                self.dicostatique[mot] += 1
            else:
                self.dicostatique[mot] = 1
        return [self.liste_mot, self.dicostatique]
    
    def cherche_binomes_mots(self):
        """la fonction principale de l'objet : faire un dictionnaire de fréquences des mots qui se suivent.
        
        arg :
            self
        return :
            dictionnaire {mot1:[mot2, mot3, mot3, mot4],...}
        """
        liste_mots_suivant = []
        #recherche des espaces délimitants les mots
        list_position_espace = []
        for i in range(len(self.texte)):
            if self.texte[i] == " ":
                list_position_espace.append(i)
        #print(list_position_espace)
        #recherche doublons mot
        debut1 = 0
        for i in range(len(list_position_espace)-2): #AFAIRE : ATTENTION ça ne prends pas les deux derniers mot. A vérifier.
            fin1 = list_position_espace[i]
            fin2 = list_position_espace[i+1]
            #print(debut1, fin1,fin2)
            mot1 = self.texte[debut1:fin1]
            mot2 = self.texte[fin1:fin2]
            debut1 = list_position_espace[i]
            #print(mot1,mot2)
            liste_mots_suivant.append([mot1,mot2])
        #print(liste_mots_suivant)
        #fait un dictionnaire avec toutes les occurences possible après un même mot.
        #les doublons sont normaux, cela veut dire que le mot revient plusieurs fois, cela correspond au calcul de leur fréquence   
        for j in range(len(liste_mots_suivant)):
            if liste_mots_suivant[j][0] in self.dicodoublons.keys():
                #print('doublons')
                self.dicodoublons[liste_mots_suivant[j][0]].append(liste_mots_suivant[j][1])
            else:
                #print('nouveau')
                self.dicodoublons[liste_mots_suivant[j][0]]=[(liste_mots_suivant[j][1])]   


class articleauhasard():
    """génére un texte aléatoire à partir d'un dictionnaire
    
        arg :
            dictionnaire {mot1:[mot2, mot3, mot3, mot4],...}
            typiquement le dictionnaire généré par le return de cherche_binomes_mots(), ou d'une sauvegarde issus de cette fonction.
        
        return
            une chaine de texte avec les mots du dictionnaire dans un ordre aléatoire.
            elle pourra aller dans un doc txt pour sauvegarde
    """

    def __init__(self, mondico):
        """initilisation
        
            arg: 
                une chaine de texte (si possible longue)
        """
        self.mondico = mondico #le dictionnaire sur lequel on travail
        self.textealeatoire="" #le texte que l'on veut
    
    def choixmotpourcommencer(self):
        """a utiliser pour le premier mot, mais aussi si un mot ne peut pas en trouver d'autre, faire une proposition piour eviter une erreur et continuer """
        pass

    def chercherlemotsuivant(self):
        """à partir d'un mot, sortir aléatoire un mot dans ceux pouvant le suivre"""
        pass
    
    def genereruntexte(self):
        """intier avec choixmotpourcommencer(), puis enchainer chercherlemotsuivant() """
        pass


def testarticledepresse():
    """3 versions de tailles différentes"""
    #enchainement logique
    a = articlepresse(textetest2)
    a.retirer_ponctuation()
    a.liste_et_compte_mots(a.texte)
    print(a.dicostatique)
    #a.cherche_binomes_mots()
    #print(a.dicodoublons)


def testarticleauhasard():
    # 5 dictionnaire issues des phrases de test via testarticledepresse
    pass
   

def main():
    testarticledepresse()
    #testarticleauhasard()
    

if __name__ == "__main__":
    main()