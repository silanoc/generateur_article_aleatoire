#! /usr/bin/env python3
# coding: utf-8

"""
modéle
pour console et fenetre graphique
"""


class articlepresse():
    """chaque article qui servira d'entrée en apprentissage sera mis dans un objet pour analyse, extraction..."""
    
    def __init__(self, text):
        """initilisation
        - arg: une chaine de texte (si possible longue)
        """
        self.texte = text
    
    def retirer_ponctuation(self):
        """ La première version du logiciel est sommaire. Pour se simplifier la vie, il faut supprimer tous les signe de ponctuations.
        Il n'y a ni entrée (arg) ni sortie (return), c'est 'juste' une modification sur l'objet"""
        ponctuation = [",",";",":","!","?",".","/","«","»",'"',"–"]
        for c in ponctuation:
            self.texte = self.texte.replace(c, "")
    
    def liste_et_compte_mots(self):
        """Compte le nombre d'occurence d'un mot.
        créé un peu par erreur, mais peu être utile pour faire des statistiques.
        arg : self
        return : dictionnaire {mot:nb}"""
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
        return dicostatique
    
    def cherche_binomes_mots(self):
        liste_mots_suivant = []
        #recherche des espaces délimitants les mots
        list_position_espace = []
        for i in range(len(self.texte)):
            if self.texte[i] == " ":
                list_position_espace.append(i)
        #print(list_position_espace)
        #recherche doublons mot
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
        #print(liste_mots_suivant)
        #fait un dictionnaire avec toutes les occurences possible après un même mot.
        #les doublons sont normaux, cela veut dire que le mot revient plusieurs fois, cela correspond au calcul de leur fréquence
        dicodoublons={}
        for j in range(len(liste_mots_suivant)):
            if liste_mots_suivant[j][0] in dicodoublons.keys():
                #print('doublons')
                dicodoublons[liste_mots_suivant[j][0]].append(liste_mots_suivant[j][1])
            else:
                #print('nouveau')
                dicodoublons[liste_mots_suivant[j][0]]=[(liste_mots_suivant[j][1])]
        print(dicodoublons)     

            
def testdumoment():
    """3 versions de tailles différentes"""
    textetest1 = "Près de dix ans après la présidentielle de 2012, Nicolas Sarkozy a été condamné jeudi 30 septembre, par le tribunal correctionnel de Paris, à un an de prison ferme pour financement illégal de campagne. Treize autres personnalités étaient également jugées dans ce qu’on appelle l’affaire Bygmalion. L’enquête et le procès ont mis à jour un vaste système de fausses factures impliquant des responsables de Bygmalion et de sa filiale Event & Cie, mais aussi des membres éminents de l’Union pour un mouvement populaire (UMP, devenue Les Républicains en 2015) et de l’équipe de campagne de Nicolas Sarkozy. A quoi correspond « l’affaire Bygmalion » ? Bygmalion, ainsi que sa filiale Event & Cie, est une agence de communication qui a organisé les meetings du candidat Sarkozy en 2012 ainsi que plusieurs conventions pour l’UMP. La société a été dirigée de 2009 à 2013 par Bastien Millot, un proche de Jean-François Copé dont il a été le chef de cabinet à la mairie de Meaux. L’UMP est accusée d’avoir organisé un système de fausses factures afin que les dépenses de campagne de Nicolas Sarkozy pour l’élection présidentielle de 2012 restent inférieures au plafond autorisé par la loi. Une partie des frais occasionnés par la campagne du candidat de la droite n’était pas réglée par l’Association pour le financement de la campagne de Nicolas Sarkozy, comme cela aurait dû être le cas. Bygmalion, l’entreprise prestataire de la campagne, les facturait en réalité à l’UMP, au prétexte d’événements plus ou moins fictifs. Le principe permettait à la campagne de M. Sarkozy de ne pas dépasser le montant de dépenses autorisé, tout en bénéficiant de prestations (l’organisation de meetings, notamment) indûment facturées au parti. Officiellement, au lieu des meetings de campagne, ce sont des conventions thématiques organisées pour l’UMP qui ont été facturées. Les révélations successives dans la presse ont montré que ces dernières représentaient un coût largement exagéré. Certaines n’ont laissé aucun souvenir à leurs participants – des élus de l’UMP –, comme le racontait Libération en révélant l’affaire : elles étaient fictives. L’enquête des juges d’instruction a démontré que le prix réel des 44 meetings organisés par l’agence événementielle Bygmalion avait été drastiquement réduit, 80 % des factures ont disparu. Le Conseil constitutionnel, confirmant une décision de la Commission nationale des comptes de campagne et des financements politiques, avait invalidé en juillet 2013 les comptes du candidat de l’UMP, après avoir constaté un dépassement des plafonds de dépenses autorisés – ce qui avait annulé le remboursement des frais de campagne. Le tribunal a établi que le montant du dépassement des comptes de campagne de Nicolas Sarkozy était de 16 247 509 euros. Qui a été jugé par le tribunal correctionnel ?"
    textetest2 = "Près de dix ans après la présidentielle de 2012, Nicolas Sarkozy a été condamné jeudi 30 septembre, par le tribunal correctionnel de Paris, à un an de prison ferme pour financement illégal de campagne. Treize autres personnalités étaient également jugées dans ce qu’on appelle l’affaire Bygmalion. L’enquête et le procès ont mis à jour un vaste système de fausses factures impliquant des responsables de Bygmalion et de sa filiale Event & Cie, mais aussi des membres éminents de l’Union pour un mouvement populaire (UMP, devenue Les Républicains en 2015) et de l’équipe de campagne de Nicolas Sarkozy. A quoi correspond « l’affaire Bygmalion » ? Bygmalion, ainsi que sa filiale Event & Cie, est une agence de communication qui a organisé les meetings du candidat Sarkozy en 2012 ainsi que plusieurs conventions pour l’UMP." 
    textetest3 = "Près de dix ans après la présidentielle de 2012, Nicolas Sarkozy a été condamné jeudi 30 septembre,"
    """un texte autre texte"""
    textetest4 = "Affaire Bygmalion : le résumé pour tout comprendre, Affaire Bygmalion : le résumé pour tout comprendre AFFAIRE BYGMALION - Nicolas Sarkozy a été renvoyé en procès pour financement illégal de campagne. De quoi parle-t-on lorsqu'on évoque l'affaire Bygmalion ? Retour sur la chronologie des révélations. Nicolas Sarkozy et 13 autres personnes sont renvoyés en procès par le juge d'instruction Serge Tournaire : l'enquête sur ses dépenses de campagne lors de la présidentielle de 2012 et les fausses factures de la société Bygmalion prend une autre tournure pour l'ancien président de la République. Nicolas Sarkozy avait été mis en examen en septembre dernier pour 'financement illégal de campagne électorale' de 2012. Il est soupçonné d'avoir approuvé la mise en place d'un système de double facturation destiné à ne pas dépasser le plafond légal pour ses comptes de campagne, fixé légalement à 22,5 millions d'euros. Ses équipes auraient demandé à la société d'événementiel Bymalion de facturer certaines dépenses à l'UMP plutôt qu'à l'association pour le financement de la campagne du président sortant. A l'origine du feuilleton politico-judicaire, on trouve les révélations du Point en février 2014 sur cette société spécialiste de l'événementiel, qui a touché huit millions d'euros pour l'organisation des meetings de campagne de Nicolas Sarkozy en 2012. Sont révélés des facturations légèrement supérieures à celles pratiquées sur le marché. A la direction de cette entreprise, deux proches de Jean-François Copé, alors président de l'UMP. Voilà donc lancée la première polémique : les soupçons de connivence et d'enrichissements personnels des dirigeants de Bygmalion grâce à leurs relations. Ses suppositions vaudront à Jean-François sa place de patron du parti. La société Bygmalion suspectée de copinage et de surfacturation Rapidement, Libération révèle le pot aux roses. Le scandale est bien plus important que présenté auparavant : durant la dernière campagne de Nicolas Sarkozy, l'UMP a déboursé des fortunes, au moins 18 millions d'euros à Bygmalion pour l'organisation d'événements, dont certains n'ont pas eu lieu comme présentés sur les facturations. La justice va donc être amenée à comprendre dans quel but des fausses factures ont été produites. Jean-François Copé, soupçonné d'enrichissement personnel, a été blanchi. Jérôme Lavrilleux, le directeur adjoint de la campagne de Nicolas Sarkozy, proche de Jean-François Copé, expliquera sur BFMTV en mai 2014 que le coût des réunions publiques étaient devenues hors de contrôle, en évoquant un 'engrenage irrésistible d'un train qui file à grande vitesse et où les personnes qui devaient tirer sur le signale d'alarme ne l'ont pas fait'. 'Il s'agit de dépenses qui ont explosées', ajoutait-il, révélant des prestations facturées de manière illégale au candidat à la présidentielle. Un système frauduleux de double facturation mis au jour Après quelques mois, l'enquête révélé que les comptes de campagne de Nicolas Sarkozy ont explosé. Son équipe de campagne aurait alors proposer à Bygmalion de maquiller certaines facturations afin qu'une partie des meetings soit payée par l'UMP, et non par l'association pour le financement de la campagne du président sortant. Une manoeuvre illégale visant à ce que le dépassement du plafond des  comptes de campagne - fixé à 22,5 millions d'euros - soit invisible. Me Maisonneuve, l'avocat de Bygmalion, a assuré que le montant des 'fausses factures' approchait les 10 millions d'euros : 'Ce qui a été facturé sous le libellé 'conventions', ce sont les meetings de campagne de Nicolas Sarkozy', a-t-il déclaré en mai 2014. L'office anti-corruption de la police judiciaire estime aujourd'hui que l'UMP a réglé 18,5 millions d'euros en fausses factures pour des événements qui n'ont pas eu lieu. Nicolas Sarkozy était-il informé ? L'affaire se cristallise désormais sur une question : qui était au courant du système de double facturation mis en place durant la campagne ? Nicolas Sarkozy a toujours assuré qu'il n'était au courant de rien et qu'il n'a jamais été informé, ni du risque de dépassement, ni de la mise en place d'un système frauduleux de fausses factures. Plusieurs collaborateurs de l'ancien président assurent pourtant qu'il était bien informé. Guillaume Lambert, son directeur de campagne, a maintenu sa version des faits devant la police : il aurait personnellement informé Nicolas Sarkozy qu'il serait difficile de maintenir un rythme soutenu de meetings, car le risque de dépassement des frais de campagne était important. Une note de l'expert-comptable de l'UMP exposant les risques a même été adressée à l'ancien chef de l'Etat en pleine campagne présidentielle. La justice s'interroge également sur un SMS, envoyé par par Jérôme Lavrilleux, le 28 avril 2012, à Guillaume Lambert. L'objet du message : de vives inquiétudes concernant le coût d'un énième meeting dans le Puy-de-Dôme. : 'Jean-François ne vient pas à Clermont, il y est allé la semaine dernière. Louer et équiper la deuxième halle est une question de coût. Nous n'avons plus d'argent. JFC [Jean-François Copé, ndlr] en a parlé au PR [président de la République, ndlr]'. Franck Attal, l'homme à la tête de la branche 'événementiel' de Bygmalion durant la campagne, concède de jamais avoir parlé directement avec Nicolas Sarkozy des fausses facturations. Pour autant, il assure que ce dernier ment, lorsqu'il déclare qu'ils ne se connaissent pas. 'On s'est croisés quarante-cinq fois sur les meetings, il m'a suivi quarante-cinq fois pas à pas pour retrouver son pupitre, (…) mais en 2016, il ne me connaît pas', ironise-t-il, dans un reportage diffusé par Envoyé Spécial le 29 septembre. 13 personnes avaient été mises en examen dans le cadre de cette enquête en septembre. Le procureur de Paris a fait savoir que Nicolas Sarkozy a été mis en examen début septembre pour 'financement illégal de campagne électorale' pour avoir 'en qualité de candidat, dépassé le plafond légal de dépenses électorales'. Trois cadres de l UMP ont également été mis en examen, pour 'faux, usage de faux et abus de confiance' : Eric Cesari, ancien directeur général adjoint de l UMP, Pierre Chassat, ancien directeur de la communication, Fabienne Liadze, ex-directrice financière."
    """test des méthodes de l'objet"""
    textetest5 = textetest1 + textetest4
    a = articlepresse(textetest3)
    a.retirer_ponctuation()
    #print(a.texte)
    print(a.liste_et_compte_mots())
    a.cherche_binomes_mots()
    

def main():
    testdumoment()
    

if __name__ == "__main__":
    main()