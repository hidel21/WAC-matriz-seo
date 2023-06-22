# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:52:58 2023

@author: darwi

esta funcion es para determinar si la keyword está subrayada entre etiquetas, pero  separadando sus palabras


"""
from expresion_regular import match_keyword
from palabra_en_kw_resaltada import palabra_kw_resaltada

def keyword_subrayada_separada(keyword, primer_parrafo, parrafo):
    
        palabras = keyword.split()
        keyword_subrayada_por_palabra = True
        # verificar si están las palabras de la kw subrayada separadamente
        for palabra in palabras:
            print("PALABRA:", )
            match = match_keyword(palabra, primer_parrafo, parrafo, 1)
            if not match:
                keyword_subrayada_por_palabra = False
         
        
        if keyword_subrayada_por_palabra == False:
            
             for palabra in palabras:
                 palabra_sola_resaltada = palabra_kw_resaltada(parrafo, palabra)
               
                  # si es true, es posible que este resaltada solo una parte de la kw, revision manual necesaria
                 if palabra_sola_resaltada:
                     return "NO CONCLUYENTE", "SI", False 
             
        return "SI", "SI", False