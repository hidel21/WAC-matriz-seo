# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:40:35 2023

@author: darwi
"""
from bs4 import BeautifulSoup, NavigableString, Tag
from quitar_acentos import quitar_acentos

def texto_no_resaltado(parrafo,keyword):
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
    all_children_have_same_tag = True
    tag = None
    attrs = None
    keyword_completa_no_subrayada = False
    print("keyword: ", keyword)
    for child in parrafo:
      print("child: ", child)
      if isinstance(child, NavigableString): # si es un parrafo de texto 
        texto = quitar_acentos(str(child.get_text())).lower()
        if keyword in texto:
            keyword_completa_no_subrayada = True
        all_children_have_same_tag = False
        continue
    # si entra aqui ya all_children_have_same_tag = False
      if isinstance(child, Tag):
            texto = quitar_acentos(str(child.get_text())).lower()
           # print(texto)
            print ("TEXTO:", texto)
            if  keyword in texto and child.name in ['b', 'span', 'i', 'em', 'strong', 'u', 'a']:
                print("Entro a if")

                kw_inside_tags = True
                
            
            if tag is None:
                tag = child.name
                attrs = child.attrs
            else:
                if child.name != tag or child.attrs != attrs:
                    all_children_have_same_tag = False
                    
                   # return True
        #print("Entro a keyword resaltada")
        
    if kw_inside_tags == False:
              return False,  keyword_completa_no_subrayada
          
    elif kw_inside_tags == True:
            if all_children_have_same_tag == True:
                print("Entro have same tag: TRUE")
                return False,  keyword_completa_no_subrayada
            else:
                return True,  keyword_completa_no_subrayada
        
   

            
     
        
        
        