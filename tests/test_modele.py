#! /usr/bin/env python3
# coding: utf-8

from modele import *

class Test_modele():
    
    def test_retirer_ponctuation(self):
        chaine = "Le, petit chat d'Hercule est mort !"
        textdebase = articlepresse(chaine)
        retirer = textdebase.retirer_ponctuation(chaine)
        assert retirer == "Le petit chat d Hercule est mort "