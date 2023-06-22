# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 08:44:49 2022

@author: darwi

obtener fecha de publicación de una página web

"""

from htmldate import find_date

    
def formato_fecha(date):
    fecha = f"{date}".split()[0] #obtenemos solo la fecha YYYY-MM-DD
    year,month,day = fecha.split("-") #separamos cada parte
    #print(year,month,day)
    #creamos un diccionario con todos los meses
    months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 
              6:"Junio", 7:"Julio", 8:"Agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
    #retornamos el resultado
    return f"{day} de {months[int(month)]} del {year}"



def obtener_fecha (url,soup):
    
    if soup.find("meta", attrs={"property": "article:published_time"}) :
        date = soup.find("meta", attrs={"property": "article:published_time"}).get("content")[0:10]
        
        return formato_fecha(date)
    elif soup.find("meta", attrs={"name": "article:published_time"}):
        date = soup.find("meta", attrs={"name": "article:published_time"}).get("content")[0:10]
        return formato_fecha(date)

    
    else:
        
        # try: 
        #         find_date(url)
        #         date= find_date(url)
        #         return formato_fecha(date)
        # except: #ValueError:
                return "FECHA NO ENCONTRADA"
    



