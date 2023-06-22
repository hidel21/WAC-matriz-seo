# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:05:50 2022

@author: darwi
"""

import unicodedata

# Funcion para quitar tildes de las vocales
def quitar_acentos(string):
    

    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    resultado = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', string).translate(trans_tab))

    return resultado