# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:10:31 2023

@author: darwi
"""

from bs4 import BeautifulSoup, NavigableString, Tag
from quitar_acentos import quitar_acentos
def palabra_kw_resaltada(parrafo,keyword):
    """
    

    Parameters
    ----------
    parrafo : TYPE
    Funcion para determinar si una keyword esta resaltada en el parrafo,
    si se diferencia visualmente del resto del texto

    Returns
    -------
    bool
        DESCRIPTION.

    """

    
    kw_inside_tags = False
    
    for child in parrafo:
            texto  = quitar_acentos(str(child.get_text())).lower()
            if  keyword in texto and child.name in ['b', 'span', 'i', 'em', 'strong', 'u', 'a']:

                kw_inside_tags = True
                
              # return True
                print("Entro una palabra de toda la kw resaltada")
        
    if kw_inside_tags == False:
              return False
          
    else:
        return True
            
        
   

            
        
        