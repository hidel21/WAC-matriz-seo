# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:50:41 2022

@author: darwi
"""
#from dateutil.parser import parse
import re
from quitar_acentos import quitar_acentos

def longitud(url):
    
    if len(url) < 100:
        url_tam = "SI"
    else:
        url_tam = "NO"
        
    return url_tam



def reemplazar_caracteres(string, caracter1, caracter2, caracter3=None, caracter4=None):
    
    if caracter3 == None and caracter4 == None:
        resultado  = string.replace(caracter1, caracter2)
        return resultado
    else:
        resultado  = string.replace(caracter1, caracter2).replace(caracter3, caracter4)
        return resultado



    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    
def contiene_fecha(url):
    # Expresiones regulares para fechas en los formatos YYYY, YYYY/MM y YYYY/MM/DD
    date_regex1 = r"\b\d{4}\b"
    date_regex2 = r"\b\d{4}[/-]\d{2}\b"
    date_regex3 = r"\b\d{4}[/-]\d{2}[/-]\d{2}\b"

    # Combinar las expresiones regulares en una sola
    date_regex = f"({date_regex1}|{date_regex2}|{date_regex3})"
    # Buscar fechas en la URL
    match = re.search(date_regex, url)
    if match:
        return "SI"
    return "NO"
        
   
    
def tiene_kw(url,keyword):
    
    # keyword_url = keyword.replace("ñ", "n")  
    # keyword_url = keyword.replace(".", "")
    keyword_url = reemplazar_caracteres(keyword,"ñ", "n", ".", "")
    #keyword_url = quitar_acentos(keyword) 
    
    if (len(keyword_url.split()) == 1):
       
        if keyword_url in url.lower():
            return "SI"
    
        else:
            return "NO"
    else:
        # keyword_caso1 = keyword.replace(" ", "-").replace("ñ", "n") # Si tiene más de una palabra, llevamos el keyword al formato que tiene en las urls
        # keyword_caso2 = keyword.replace(" ", "_").replace("ñ", "n")
        # keyword_caso3 = keyword.replace(" ", "").replace("ñ", "n")
        keyword_caso1 = reemplazar_caracteres(keyword, " ", "-", "ñ", "n")
        keyword_caso2 = reemplazar_caracteres(keyword, " ", "_", "ñ", "n")
        keyword_caso3 = reemplazar_caracteres(keyword, " ", "", "ñ", "n")
        
        if keyword_caso1 in url.lower() or keyword_caso2 in url.lower() or keyword_caso3 in url.lower():
            return "SI"
        
        else: # si entra en un caso particular, estudiar si esta contenida la kw, ejm: innovacion_tecnologica-/xx
            palabras = keyword.split()
            for palabra in palabras:
                palabra = palabra.replace("ñ", "n")
                if "." in palabra:
                    opc1 = palabra.replace(".", "-")
                    opc2 = palabra.replace(".", "_")
                    opc3 = palabra.replace(".", "")
                    if opc1 not in url.lower() and opc2 not in url.lower() and opc3 not in url.lower():
                        return "NO"
                elif palabra not in url.lower():
                    return "NO"
                
            return "SI"
        
    
    
        

    
    
    
    
    
    
    
    
    
    
