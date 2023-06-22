# # -*- coding: utf-8 -*-
# """
# Created on Wed Feb 15 15:40:01 2023

# @author: darwi
# """
# import re
# from quitar_acentos import quitar_acentos

# def match_keyword(keyword, parrafo, parrafos):
    
#     match = re.search(r"(<(strong|b|span|em|u|i|a).*>.?" + keyword + "[.,]?.?</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + keyword + "[.,]?.*?</strong>.*?</em>)",parrafo)

#     if match:
#        return True
   
#     elif not match:
#         kw_inside_tags = False
#         for child in parrafos:
#                 print("child: ", child)
#           # if isinstance(child, NavigableString): # si es un parrafo de texto 
#           #   texto = quitar_acentos(str(child.get_text())).lower()
#           #   if keyword in texto:
#           #       keyword_completa_no_subrayada = True
#           #   all_children_have_same_tag = False
#           #   continue
#         # si entra aqui ya all_children_have_same_tag = False
#           # if isinstance(child, Tag):
#                 texto = quitar_acentos(str(child.get_text())).lower()  #solo texto plano
#                # print(texto)
#                 print ("TEXTO:", texto)
#                 if  keyword in texto and child.name in ['b', 'span', 'i', 'em', 'strong', 'u', 'a']:
#                     print("Entro a if")

#                     kw_inside_tags = True
                    
                
                
#         if kw_inside_tags == True:
#                return True
        
        
#         #######################
#     else:
#        return False

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:40:01 2023

@author: darwi
"""
import re
from quitar_acentos import quitar_acentos

def match_keyword(keyword, parrafo, parrafos, caso):
    
    match = re.search(r"(<(strong|b|span|em|u|i|a).*>.?" + keyword + "[.,]?.?</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + keyword + "[.,]?.*?</strong>.*?</em>)",parrafo)

    if match:
       return True
   
    elif not match:
        kw_inside_tags = False
        for child in parrafos:
                print("child: ", child)
          # if isinstance(child, NavigableString): # si es un parrafo de texto 
          #   texto = quitar_acentos(str(child.get_text())).lower()
          #   if keyword in texto:
          #       keyword_completa_no_subrayada = True
          #   all_children_have_same_tag = False
          #   continue
        # si entra aqui ya all_children_have_same_tag = False
          # if isinstance(child, Tag):
                texto = quitar_acentos(str(child.get_text())).lower()  #solo texto plano
               # print(texto)
                print ("TEXTO:", texto)
                if caso == 0: # evaluar kw subrayada sin texto adicional
                    
                    if  keyword == texto and child.name in ['b', 'span', 'i', 'em', 'strong', 'u', 'a']:
                        print("Entro a if")

                        #kw_inside_tags = True
                        return True
                elif caso == 1:
                       if  keyword in texto and child.name in ['b', 'span', 'i', 'em', 'strong', 'u', 'a']:
                         print("Entro a if")

                         kw_inside_tags = True
                
                
        if kw_inside_tags == True:
               return True
        
        
        #######################
    else:
       return False