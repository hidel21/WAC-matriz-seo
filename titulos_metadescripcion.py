# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:35:32 2022

@author: ender

Extraer títulos y metadescripción
"""

# import requests
# import pandas as pd
# import urllib.request
# from urllib.parse import urlparse
# from bs4 import BeautifulSoup
from quitar_acentos import quitar_acentos
import unicodedata

def title_seo_h1_diferentes(soup,keyword):
    
    if  soup.find("title") and  soup.find("h1") :
        
        
        if len(soup.findAll("h1")) > 1 :
            title_h1 = buscar_titulo_h1(soup, keyword)
            
        else: 
            title_h1 = soup.find("h1").get_text().strip().lower()
            title_h1 = quitar_acentos(title_h1)
     
        title_seo  = soup.find("title").get_text().strip().lower()
        title_seo = quitar_acentos(title_seo)
         
         
         
        if title_seo.startswith(title_h1):
             substring = title_seo.split(" -")[0].split(" |")[0].split(" :")[0]
             if substring == title_h1 :
                 return "SI"
        else:
             return "NO"
    
    else:
        return "NULL"

def obtener_title_seo(soup,keyword):
    """Return the page title

    Args:
        soup: HTML code from Beautiful Soup
        
    Returns: 
        value (string): Parsed value
    """
    

    if soup.findAll("title"):
        title_seo = soup.find("title").get_text().strip()
        title_seo = quitar_acentos(title_seo).lower()
      #  title_seo = title_seo.split(" -")[0].split(" |")[0].split(" :")[0]
        # Chequear longitud
        if len(title_seo) > 70:
            len_title_seo = "No"
        else:
            len_title_seo = "SI"
            
        # Chequear si contiene el keyword
        if keyword in title_seo:
            have_kw =  "SI"
        else:
            have_kw =  "NO"
            
        return len_title_seo, have_kw
        
    else:
        return "Titulo SEO no encontrado", "Nulo"

    
def buscar_titulo_h1(soup, keyword):
    
    titulos = soup.findAll("h1")
    title = ""
    for titulo in titulos:
        title = titulo.get_text().strip().lower()
        title = quitar_acentos(title)
       
        if keyword in title:
            
            return title
        
    
           
       # print(title_h1)
   
    return title

def obtener_title_h1(soup,keyword):
    """Return the page title

    Args:
        soup: HTML code from Beautiful Soup
        
    Returns: 
        value (string): Parsed value
    """
       

    if soup.findAll("h1"):
        
        if len(soup.findAll("h1")) > 1 :
            title_h1 = buscar_titulo_h1(soup, keyword)
          
        else:
            
            title_h1 = soup.find("h1").get_text().strip()
            title_h1 = quitar_acentos(title_h1).lower()
           # print(title_h1)
        # chequear si contiene el keyword al inicio
        if title_h1.startswith(keyword):
            starts_with_kw = "SI"
            
       
        elif  keyword in title_h1 :  
            
                    # indice del comienzo de la keyword
                 if len(title_h1[0:title_h1.index(keyword)]) <= 14:
                    starts_with_kw = "SI"
                 else:
                     starts_with_kw = "NO"
           
        else:
            starts_with_kw = "NO"
        
        if len(title_h1) <= 70:
            len_title_seo = "SI"
        else:
            len_title_seo = "NO"
        return title_h1, len_title_seo, starts_with_kw
    else:
        return "NOT FOUND","Nulo", "Nulo"
   
    
def obtener_description(soup, keyword):
    
    """
    Función para obtener la meta descripción de la url
    
    también determina si en dicha descripción aparece el keyword
    
    """
    if soup.findAll("meta", attrs={"name": "description"}):
        description = soup.find("meta", attrs={"name": "description"}).get("content")
        description = quitar_acentos(description)
       
        
        if len(description) >= 156:
            len_description= "NO"
        else:
            len_description = "SI"
       
        if keyword in description.lower():
            have_kw =  "SI"
        else:
            have_kw =  "NO"
        return len_description, have_kw
    
    elif soup.findAll("meta", attrs={"property": "og:description"}):
        description = soup.find("meta", attrs={"property": "og:description"}).get("content")
        description = quitar_acentos(description)
        
        
        if len(description) >= 156:
            len_description= "NO"
        else:
            len_description = "SI"
       
        if keyword in description.lower():
            have_kw =  "SI"
        else:
            have_kw =  "NO"
        return len_description, have_kw
    
    else:
        return "NOT FOUND", "NULO"

    






