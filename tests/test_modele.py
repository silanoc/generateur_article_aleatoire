#! /usr/bin/env python3
# coding: utf-8

import random
import pytest
from modele import *
from unittest.mock import Mock, patch                                                                                                                                                                                 

class Test_modele_analyse():
    
    def test_retirer_ponctuation(self):
        chaine = "Le, petit chat d'Hercule est mort !"
        textdebase = Article_source(chaine)
        retirer = textdebase.retirer_ponctuation(chaine)
        assert retirer == "Le petit chat d Hercule est mort "
        
    def test_liste_et_compte_mots(self):
        chaine = "le petit chat de béatrice est sur le petit mur du jardin de Yves"
        textdebase = Article_source(chaine)
        list_mot = textdebase.liste_et_compte_mots(chaine)[0]
        dico_mot = textdebase.liste_et_compte_mots(chaine)[1]
        assert list_mot == ['le','petit','chat','de','béatrice','est','sur','le','petit','mur','du','jardin','de','Yves']
        assert dico_mot == {'le':2,'petit':2,'chat':1,'de':2,'béatrice':1,'est':1,'sur':1,'mur':1,'du':1,'jardin':1,'Yves':1}
     
    """   
    def test_cherche_binomes_mots(self):
        chaine = "le petit chat de béatrice est sur le petit mur du jardin de Yves"
        textdebase = Article_source(chaine)
        dico = textdebase.cherche_binomes_mots(chaine)
        assert dico == {' le': [' petit', ' petit'], ' petit':[' chat', ' mur'], ' chat': [' de'], ' de': [' béatrice', ' Yves'], ' béatrice': [' est'],
                        ' est': [' sur'], ' sur': [' le'], ' mur': [' du'], ' du': [' jardin'], ' jardin': [' de'], ' Yves': []}
    """ 
    
    
class Test_modele_generation():
    
    def test_choixmotpourcommencer(self, mocker):
        dictionnaire = {' le': [' petit', ' petit'], ' petit':[' chat', ' mur'], ' chat': [' de'], ' de': [' béatrice', ' Yves'], ' béatrice': [' est'],
                        ' est': [' sur'], ' sur': [' le'], ' mur': [' du'], ' du': [' jardin'], ' jardin': [' de'], ' Yves': []}
        mocker.patch('random.randint', return_value=1)
        generation = articleauhasard(dictionnaire)
        generation.mot = generation.choixmotpourcommencer(dictionnaire)
        assert generation.mot == "petit"
        
def test_addition_dico():
    dico1 = {'a' : ['le', 'petit'], 'b' : ['chat', 'de']}
    dico2 = {'b' : ['de', 'yves'], 'c' : ['dans', 'jardin']}
    dico3 = addition_dico(dico1, dico2)
    assert dico3 == {'a' : ['le', 'petit'], 'b' : ['chat', 'de', 'de', 'yves'], 'c' : ['dans', 'jardin']}