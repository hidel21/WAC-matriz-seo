# -*- coding: utf-8 -*-

import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import requests
import pandas as pd
from bs4 import BeautifulSoup
from titulos_metadescripcion import *
#import keyword_neg 
from keyword_primer_parrafo import keyword_primer_parrafo
import url as url
from obtener_fecha_publicacion import obtener_fecha
from titulos_metadescripcion import title_seo_h1_diferentes
from urllib.parse import urlparse
import re
import validators

#from titulos_metadescripcion import *
   
def verificar_enlaces(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        enlaces_internos = []
        enlaces_externos = []
        
        for enlace in soup.find_all('a'):
            href = enlace.get('href')
            
            if href:
                if validators.url(href):
                    parsed_url = urlparse(href)
                    
                    if parsed_url.netloc == urlparse(url).netloc:
                        enlaces_internos.append(href)
                    else:
                        enlaces_externos.append(href)
        
        return enlaces_internos, enlaces_externos
    
    except:
        return [], []

# Info visual de la web app
st.title("Matriz SEO")
st.write("Adjuntar archivo con las urls")
uploaded_file = st.file_uploader(label= "Elegir archivo",label_visibility= 'hidden')


# Cargar archivo
if uploaded_file is not None:

   #xls or xlsx
   file=pd.read_excel(uploaded_file)
else:
    st.warning("El archivo debe ser de tipo .xlsx")

bar = st.progress(0)

if uploaded_file: 
  
    
    # Leer archivo excel con URLs y keywords
   
    
    
    matriz_seo = pd.DataFrame( columns=['Titulo',
                                        'Categoría',
                                        'Mes producido',
                                             '¿Ya esta publicado?',
                                             'Fecha de publicacion',
                                             'Keyword',
                                             'URL',
                                             '¿El titulo SEO es de máximo 70 caracteres?',
                                             'El titulo SEO tiene el keyword',
                                             '¿La metadescripción es inferior a 156 caracteres?',
                                             '¿Aparece el keyword en la metadescripción?',
                                             '¿Aparece el keyword al inicio en el título H1?',
                                             '¿Titulo H1 inferior a 70 caracteres?',
                                             'El 25% de las oraciones sobrepasan las 20 palabras',
                                             'Está subrayado el keyword',
                                             'El keyword está en el primer párrafo',
                                             'Densidad del keyword cercana al 2%',
                                             'Contiene algún link interno',
                                             'Contiene links externos',
                                             '¿Cuándo se da clic envía a otra ventana?',
                                             '¿La URL es inferior a 100 caracteres?',
                                             'La URL no tiene fecha de publicación',
                                             'Tiene el keyword en la URL'
                                             #'¿Título SEO y H1 diferentes?' # añadido
                                             ])
    
     
    
    print("Obteniendo datos de las URLs...")
    print("\n")
    
    
    # lista para llevar un control de los comentarios de titulo H1 y SEO iguales
    titles_h1_seo_same =[]
    
    
    # lista para llevar un control del caso especial donde la keyword esta
    # subrayada junto a toda una oración/frase
    sub_caso_special =[]
    
    # lista para mostrar mensaje de titulo seo no vinculante
    title_seo = []
    
    kw_faltantes = []
    url_faltantes = []

    with st.container():
        for i in range(len(file)):
            
           
            
             # si falta la url o el keyword #i en el archivo
            if ( pd.isna(file.loc[i][0])  or pd.isna(file.loc[i][1]) or  not (validators.url(file.loc[i][0])) ):
                
                matriz_seo.loc[i] = ["NULO" ,  
                                     "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO",
                                    "NULO"
                                 ]
                
                # se añade un null a la lista de comparación de titulos y caso especial
                # para mantener la misma longitud
                titles_h1_seo_same.append(" ")
                sub_caso_special.append(False)
                title_seo.append(None)
                
                if (pd.isna(file.loc[i][0])  or not (validators.url(file.loc[i][0]))):
                    
                    url_faltantes.append(i+2);
                    
                if ( pd.isna(file.loc[i][1]) ):
                    kw_faltantes.append(i+2)
                    
                    
                continue
                
                
               # with st.sidebar:
                
                   # string = "Falta la url o la keyword #%s. Aplicación detenida"%(i+2)
                   # st.warning(string,icon="⚠️")
                  
                  #  st.stop # se detiene la app
                    
            #  Manejar el error de SSL certificate
            
            try: 
                try:
                    page = requests.get(file.loc[i][0],headers= {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
                except:
                    page = requests.get(file.loc[i][0],headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'} )

            except:
                try:
                    page = requests.get(file.loc[i][0],headers= {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},verify=False)
                except:
                    page = requests.get(file.loc[i][0],headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}, verify= False )
           
            keyword = file.loc[i][1]
            
            # validación para ignorar todo caracter que no sea una letra o un número en la keyword
            #keyword = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ-Z0-9 ]', '', keyword)
            keyword = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ-Z0-9. ]', '', keyword) # no eliminar puntos
            if keyword[-1] == "-" or keyword[-1] == ".":
                keyword = keyword.rstrip(keyword[-1])
            if keyword[0] == "-" or keyword[0] == ".":
                 keyword = keyword.rstrip(keyword[0])   
                
            keyword = keyword.strip().lower()
            keyword = quitar_acentos(keyword)
            keyword=  " ".join( keyword.split() ) # eliminar espacios dentro de la keyword
            # por ejemplo "la  comunicación" (hay 1 espacio adicional)
            
            # añadir validación si la página está disponible
            if "404"  in str(page):
                
                matriz_seo.loc[i] = ["ERROR 404" ,  
                                     ' ',
                                    ' ',
                                    "ERROR 404" ,
                                   "ERROR 404" ,
                                    keyword,
                                    file.loc[i][0] ,
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404",
                                    ' ',
                                    ' ',
                                    ' ',
                                    "ERROR 404",
                                    "ERROR 404",
                                    "ERROR 404"
                                 ]
                
                # se añade un null a la lista de comparación de titulos y caso especial
                # para mantener la misma longitud
                titles_h1_seo_same.append("NULL")
                sub_caso_special.append(False)
                title_seo.append(None)
                continue
            
            
            #####################################################
            
            soup = BeautifulSoup(page.content, 'html.parser')
           
            
            len_title_seo, have_kw_title_seo = obtener_title_seo(soup, keyword)
            len_description, have_kw_meta_description = obtener_description(soup, keyword)
            title_h1, len_title_h1, starts_with_kw= obtener_title_h1(soup, keyword)
            
            #se añade a la lista un SI o NO, dependiendo si el titulo H1 Y seo son iguales
            titles_h1_seo_same.append(title_seo_h1_diferentes(soup,keyword))
            kw_subrayada, kw_primer_parrafo, caso_especial = keyword_primer_parrafo(soup, keyword)
            
            # se añade False o True si se da el caso especial de kw subrayada
            sub_caso_special.append(caso_especial)
            title_seo.append(have_kw_title_seo)

            #se añaden una verificacion de enlaces segun sea el caso
            enlaces_internos, enlaces_externos = verificar_enlaces(file.loc[i][0])
            if len(enlaces_internos) > 0:
                internos = 'SI'
            else:
                internos = 'NO'
                
   
            if len(enlaces_externos) > 0:
                externos = 'SI'
            else:
                externos = 'NO'

            matriz_seo.loc[i] = [title_h1 ,  
                                 ' ',
                                ' ',
                                'SI',
                                obtener_fecha(file.loc[i][0], soup),
                                keyword,
                                file.loc[i][0],
                                len_title_seo,
                                have_kw_title_seo,
                                len_description,
                                have_kw_meta_description,
                                starts_with_kw,
                                len_title_h1,
                                'NO',
                               kw_subrayada,
                               kw_primer_parrafo,
                                'SI',
                                internos,
                                externos,
                                externos,
                                url.longitud(file.loc[i][0]),
                                url.contiene_fecha(file.loc[i][0]),
                                url.tiene_kw(file.loc[i][0], keyword)
                             ]
                                
         
            
            print("URLS PROCESADAS: ",i+1)
            print("keyword :", keyword)
            bar.progress(int(100 * (i+1) / len(file)) )
            st.write( "URLS PROCESADAS: ",i+1 )
            st.write("keyword :", keyword)
          
            
        # fin del recorrido de las urls
        ########################################
    
        from io import BytesIO
        output = BytesIO()
        # crear archivo Excel
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        
        # Convertir Dataframe a excel
        matriz_seo.to_excel(writer, sheet_name='MATRIZ DE SEO', index=False)
        
       
        # Get workbook
        workbook = writer.book
        
        # Get Sheet1
        worksheet = writer.sheets['MATRIZ DE SEO']
        
        cell_format = workbook.add_format()
        cell_format.set_font_name('Century Gothic')
        cell_format.set_font_size(11)
        cell_format.set_border()
        worksheet.set_column('A:Z', None, cell_format)
        
      #  f1=workbook.add_format({'bold':True, 'font_color':'blue'})
        blue = workbook.add_format({'font_color':'blue'})
        

        # background = workbook.add_format({'bg_color': '#44546A'})

        # # Add the rule to column A.
        # x= str(len(file)+1)
        # formato = 'H2:W'+x
        # worksheet.conditional_format(formato, {'type': 'cell',
        #                              'criteria': 'equal to',
        #                              'value': '"NO"',
        #                              'format': background})
        
        
        #------------- añadir comentarios al excel  ------------#
        for i in range(len(file)):
            if titles_h1_seo_same[i] == 'SI':
              #  worksheet.write('A1', 'Hello')
                worksheet.write_comment('M%s'%(i+2), 'Título H1 duplicado')
        
            if sub_caso_special[i]==True:
                worksheet.write_comment('O%s'%(i+2), 'Hay texto adicional subrayado junto con la palabra clave')
        
            if (title_seo[i] == 'NO'):
                worksheet.write_comment('I%s'%(i+2), 'Título diferente al propuesto')
                
            # cambiar formato para mensaje especial
            if matriz_seo.loc[i][14] == "NO CONCLUYENTE":
             #  worksheet.set_font('i+2', 'O', font={'color': 'red', 'bold': True})
           #   worksheet.write('O%s'%(i+2), bold)
             #  worksheet.set_format(int(i+2), 14, bold)
               worksheet.write(int(i+1), 14, 'NO CONCLUYENTE', blue)


        #----------------------------------------------
        writer.close()
        
      
        with st.sidebar:
            
            st.download_button(label='Descargar archivo', data=output.getvalue(), file_name='MATRIZ SEO.xlsx',mime="application/vnd.ms-excel",     
                               on_click=st.stop)
            
            if (len(url_faltantes) != 0):
                string = "Faltan una url o no es válida: " if len(url_faltantes) == 1 else "faltan algunas urls o no son válidas: "
                st.warning(string,icon="⚠️")
                texto = "fila: " if len(url_faltantes) == 1 else "filas: "
                print(texto)
                st.write(texto)
                st.text(str(url_faltantes).replace("[", "").replace("]", ""))
                    
            if (len(kw_faltantes) != 0):
                
                string = "Faltan algunas keywords: " if len(kw_faltantes) == 1 else "falta una keyword: "
                st.warning(string,icon="⚠️")
                texto = "fila: " if len(kw_faltantes) == 1 else "filas: "
                print(texto)
                st.write(texto)
                st.text(str(kw_faltantes).replace("[", "").replace("]", ""))
