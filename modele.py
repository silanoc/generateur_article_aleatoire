#! /usr/bin/env python3
# coding: utf-8

"""
modéle
pour console et fenetre graphique
"""


class articlepresse():
    """chaque article qui servira d'entrée en apprentissage """
    
    def __init__(self, text):
        self.texte = text
    
    def retirer_ponctuation(self):
        ponctuation = [",",";",":","!","?",".","/","«","»",'"',"–"]
        for c in ponctuation:
            self.texte = self.texte.replace(c, "")
    
    def liste_et_compte_mots(self):
        dicostatique = {}
        debut = 0
        fin = 0
        for i in range (len(self.texte)):
            if self.texte[i] == " ":               
                fin = i
                mot = self.texte[debut:fin]
                if mot in dicostatique:
                    dicostatique[mot] += 1
                else:
                    dicostatique[mot] = 1
                debut = i+1
                print(dicostatique)
    
    def cherche_binomes_mots(self):
        liste_mots_suivant = []
        liste_des_listes_mots_suivant = [[]]
        #recherche des espaces délimitants les mots
        list_position_espace = []
        for i in range(len(self.texte)):
            if self.texte[i] == " ":
                list_position_espace.append(i)
        #print(list_position_espace)
        #recherhce doublons mot
        debut1 = 0
        for i in range(len(list_position_espace)-2): #ATTENTION ça ne prends pas les deux derniers mot. A vérifier.
            fin1 = list_position_espace[i]
            fin2 = list_position_espace[i+1]
            #print(debut1, fin1,fin2)
            mot1 = self.texte[debut1:fin1]
            mot2 = self.texte[fin1:fin2]
            debut1 = list_position_espace[i]
            #print(mot1,mot2)
            liste_mots_suivant.append([mot1,mot2])
        print(liste_mots_suivant)
        """
        for j in range(len(liste_mots_suivant)):
            print(liste_mots_suivant[j][0])
            if liste_mots_suivant[j] in liste_des_listes_mots_suivant:
                print('ajout')
                liste_des_listes_mots_suivant.append(liste_mots_suivant[j][1])
            else:
                print('nouveau')
            liste_des_listes_mots_suivant.append(liste_mots_suivant[j])
        """ 
        """
        for m in range(len(liste_mots_suivant)):
            for n in range(m+1,len(liste_mots_suivant)):
                print(liste_mots_suivant[n])
                print(liste_des_listes_mots_suivant)
                if liste_mots_suivant[n] in liste_des_listes_mots_suivant:
                    liste_des_listes_mots_suivant[m].append(liste_mots_suivant[n][1])
                    liste_mots_suivant.remove(liste_mots_suivant[n])
                else:
                    liste_des_listes_mots_suivant.append(liste_mots_suivant[n])
                if n>len(liste_mots_suivant)+1:
                    break
        """
        print(liste_des_listes_mots_suivant)
        #print(liste_mots_suivant)

            
def testdumoment():
    """3 versions de tailles différentes"""
    textetest1 = "Près de dix ans après la présidentielle de 2012, Nicolas Sarkozy a été condamné jeudi 30 septembre, par le tribunal correctionnel de Paris, à un an de prison ferme pour financement illégal de campagne. Treize autres personnalités étaient également jugées dans ce qu’on appelle l’affaire Bygmalion. L’enquête et le procès ont mis à jour un vaste système de fausses factures impliquant des responsables de Bygmalion et de sa filiale Event & Cie, mais aussi des membres éminents de l’Union pour un mouvement populaire (UMP, devenue Les Républicains en 2015) et de l’équipe de campagne de Nicolas Sarkozy. A quoi correspond « l’affaire Bygmalion » ? Bygmalion, ainsi que sa filiale Event & Cie, est une agence de communication qui a organisé les meetings du candidat Sarkozy en 2012 ainsi que plusieurs conventions pour l’UMP. La société a été dirigée de 2009 à 2013 par Bastien Millot, un proche de Jean-François Copé dont il a été le chef de cabinet à la mairie de Meaux. L’UMP est accusée d’avoir organisé un système de fausses factures afin que les dépenses de campagne de Nicolas Sarkozy pour l’élection présidentielle de 2012 restent inférieures au plafond autorisé par la loi. Une partie des frais occasionnés par la campagne du candidat de la droite n’était pas réglée par l’Association pour le financement de la campagne de Nicolas Sarkozy, comme cela aurait dû être le cas. Bygmalion, l’entreprise prestataire de la campagne, les facturait en réalité à l’UMP, au prétexte d’événements plus ou moins fictifs. Le principe permettait à la campagne de M. Sarkozy de ne pas dépasser le montant de dépenses autorisé, tout en bénéficiant de prestations (l’organisation de meetings, notamment) indûment facturées au parti. Officiellement, au lieu des meetings de campagne, ce sont des conventions thématiques organisées pour l’UMP qui ont été facturées. Les révélations successives dans la presse ont montré que ces dernières représentaient un coût largement exagéré. Certaines n’ont laissé aucun souvenir à leurs participants – des élus de l’UMP –, comme le racontait Libération en révélant l’affaire : elles étaient fictives. L’enquête des juges d’instruction a démontré que le prix réel des 44 meetings organisés par l’agence événementielle Bygmalion avait été drastiquement réduit, 80 % des factures ont disparu. Le Conseil constitutionnel, confirmant une décision de la Commission nationale des comptes de campagne et des financements politiques, avait invalidé en juillet 2013 les comptes du candidat de l’UMP, après avoir constaté un dépassement des plafonds de dépenses autorisés – ce qui avait annulé le remboursement des frais de campagne. Le tribunal a établi que le montant du dépassement des comptes de campagne de Nicolas Sarkozy était de 16 247 509 euros. Qui a été jugé par le tribunal correctionnel ?"
    textetest2 = "Près de dix ans après la présidentielle de 2012, Nicolas Sarkozy a été condamné jeudi 30 septembre, par le tribunal correctionnel de Paris, à un an de prison ferme pour financement illégal de campagne. Treize autres personnalités étaient également jugées dans ce qu’on appelle l’affaire Bygmalion. L’enquête et le procès ont mis à jour un vaste système de fausses factures impliquant des responsables de Bygmalion et de sa filiale Event & Cie, mais aussi des membres éminents de l’Union pour un mouvement populaire (UMP, devenue Les Républicains en 2015) et de l’équipe de campagne de Nicolas Sarkozy. A quoi correspond « l’affaire Bygmalion » ? Bygmalion, ainsi que sa filiale Event & Cie, est une agence de communication qui a organisé les meetings du candidat Sarkozy en 2012 ainsi que plusieurs conventions pour l’UMP." 
    textetest3 = "Près de dix ans après la présidentielle de 2012"
    """test des méthodes de l'objet"""
    a = articlepresse(textetest2)
    a.retirer_ponctuation()
    #print(a.texte)
    #a.liste_et_compte_mots()
    a.cherche_binomes_mots()
    

def main():
    testdumoment()
    

if __name__ == "__main__":
    main()