import calendar
import os
import platform
import sys
import urllib.request
import re
import requests
# import emojis
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import collections
import csv
import datetime
from datetime import date
from PIL import Image
from io import BytesIO
import PySimpleGUI as vent
import os
from io import StringIO
import itertools
from itertools import *
from numpy import nan 

def fecha_titulo():
    """Esta función permite que la fecha impresa en el informe producido esté en un formato específico"""
    meses =  {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre",  11: "Noviembre", 12: "Diciembre"}
    dias = { 0: "Domingo",  1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado"}
    ahora = date.today()        # se asigna la fecha actual a la variable "ahora"
    numero_mes = ahora.month    # se asigna el mes a la variable "numero mes"
    numero_dia = int(ahora.strftime("%w"))      # https://strftime.org/  VER SIGNIFICADO 
    dia = dias.get(numero_dia)                  #Obtiene el elemento "numero_dia" de dias{} que esta en formato clave:valor
    mes = meses.get(numero_mes)                 #Obtiene el elemento "numero_mes" de meses{} que esta en formato clave:valor
    fecha_hoy = "{}, {} de {} de {}".format(dia, ahora.day, mes, ahora.year)        # Permite dar a la fecha el siguiente formato: "Martes, 17 de Marzo de 2020"
    return fecha_hoy            # Retorna fecha con el formato dado

def highlight(element):
    """Resalta elemento a capturar mediante Selenium webdriver"""
    #driver = element._parent
    def apply_style(s):         #   s = "background: lightgrey; border: 2px solid red;"
        browser.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)         # Synchronously Executes JavaScript in the current window/frame
    original_style = element.get_attribute('style')                 #Gets the given attribute or property of the element.
    apply_style("background: lightgrey; border: 2px solid red;")    

def texto_tweet3i():
     texto_tweet3 = '-'
     arroba_text = '-'
     hashtag_tweet = '-'
     while texto_tweet3 !="  " and arroba_text !="  " and hashtag_tweet !=" ":
        try: 
            texto_tweet3 = browser.find_elements_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"] div[class="css-901oao r-jwli3a r-1qd0xha r-1blvdjr r-16dba41 r-ad9z0x r-bcqeeo r-19yat4t r-bnwqim r-qvutc0"] > span')  # Busca y obtiene un HTML que contiene texto (en caso de haber) del tweet
            texto_tweet3 = [x.text for x in texto_tweet3]           # Arma una lista en caso de encontrar más de un texto en el tweet
        except:
            texto_tweet3 = " "          # Ejecuta la excepción en los espacios vacíos para que el programa siga ejecutando y no tire un error
        try:
            arroba_text = browser.find_elements_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"] div[class="css-901oao r-jwli3a r-1qd0xha r-1blvdjr r-16dba41 r-ad9z0x r-bcqeeo r-19yat4t r-bnwqim r-qvutc0"] > div> span > a') # Busca y obtiene un HTML que contiene texto (en caso de haber) de contenido @arrobado
            arroba_text = [x.text for x in arroba_text]             # Arma una lista en caso de encontrar más de una palabra arrobada en el tweet
        except:
            arroba_text = " "                                      # Ejecuta la excepción en los espacios vacíos para que el programa siga ejecutando y no tire un error
        num = min(len(texto_tweet3), len(arroba_text))              # The min() function returns the smallest of the input values.
        result = [None]*(num*2)                                     # Hace que todos los elementos de "result" sean un None. Ej:result=[None,None,None,None,None,None] (suponiendo que num=3)
        result[::2] = texto_tweet3[:num]                            # Reemplaza los elementos result[0],result[2],result[4],etc por texto_tweet3[0],texto_tweet3[2], texto_tweet3[4], etc.
        result[1::2] = arroba_text[:num]                            # Reemplaza los elementos result[1],result[3],result[5],etc por arroba_text[1],texto_tweet3[3], texto_tweet3[5], etc.
        result.extend(texto_tweet3[num:])                           # Hace un "append()", es decir, adjunta texto_tweet3 a result. (CONSULTAR)                          
        return result                                               # Retorna resultado
user_profile = os.environ['USERPROFILE']                            # "os.environ" in Python is a mapping object that represents the user’s environmental variables. It returns a dictionary having user’s environmental variable as key and their values as value. For example, environ['HOME'] is the pathname of your home directory (on some platforms)                        
options = Options()                                                 # Se crea un objeto del tipo Options()
options.add_argument("--disable-notifications")                     # Deshabilita notificaciones         
options.add_argument("--disable-infobars")                          # Deshabilita barras de información
options.add_argument("--mute-audio")                                # Deshabilita el audio
options.add_argument("--user-data-dir=" + user_profile + "/AppData/Local/Google/Chrome/User Data/")     # consultar
options.add_argument("--profile-directory=Default")                 # The user data directory is the parent of the profile directory.
browser = webdriver.Chrome(executable_path="./chromedriver.exe",options=options)    # Driver utilizado para iniciar el navegador(o browser)

vent.theme ('Light Blue 2')                                         # vent es un objeto de tipo PySimpleGUI
# configuración de la interfaz
layout = [  [vent.Text('URL TWEET'), vent.Text(size=(6, 1))],
            [vent.InputText(size=(55, 2))],
            [vent.Text('TITULO DESCRIPTIVO'), vent.Text(size=(3, 1))],
            [vent.InputText(size=(55, 2))],
            [vent.Text('DESCRIPCION CUENTA'), vent.Text(size=(3, 1))],
            [vent.Multiline(size=(55, 10))],                     
            [vent.Text('SOBRE REPERCUSION'), vent.Text(size=(3, 1))],
            [vent.Multiline(size=(55, 10))],
            [vent.Text('ARCHIVO', size=(8, 1)), vent.Input(key='path'),  vent.FileBrowse()],
            [vent.Button('CREAR NUEVO REPORTE'), vent.Button('GUARDAR EN REPORTE'), vent.Button('SALIR')]]



window = vent.Window('CAPTURA TWITTER - DIVISION CIBERINTELIGENCIA', layout, keep_on_top=False, auto_size_buttons=True) # ejecución de la ventana o interfaz
while True:
    pass
    event, values = window.read()               
    if event in  (None, 'SALIR'):                       # si se elige "SALIR", se cierra el browser
        browser.close()  
        break
    if event == 'CREAR NUEVO REPORTE':                  # Evento consistente en la creación de un nuevo reporte
        director = datetime.datetime.now().strftime("%d-%m-%y_%H_%M_%S")    # directorio toma el valor (path) siguiente: (Bangho 5/Documents/director)
        directorio = user_profile + "/Documents/" + director                #/Bangho 5/Documents/datetime.datetime.now().strftime("%d-%m-%y_%H_%M_%S")
        window['path'].update(directorio)                       # Se agrega al "path"                
        if not os.path.exists(directorio):                      # Pregunta si existe un archivo. En caso de no existir, crea uno mediante os.mkdir
            os.mkdir(directorio)                                # crea el "directorio"
            os.mkdir(directorio +'/salida')                     # crea una carpeta llamada "salida" (dentro de directorio)
            os.mkdir(directorio +'/salida/imagenes')            # crea una carpeta llamada "imagenes" dentro de "salida"
            os.mkdir(directorio +'/salida/imagenes/comentarios')    # crea la carpeta "comentarios" dentro de "imagenes"
            os.mkdir(directorio +'/salida/screenshots')             # crea la carpeta "screenshots" dentro de "salida"
            os.mkdir(directorio + '/salida/screenshots/usuarios')   # crea la carpeta "usuarios" dentro de "screenshots"
        fp = open(os.path.join(directorio +"/salida/busquedas.html"), "a")  # Junta los paths en "fp" quedando: /Bangho 5/Documents/datetime.datetime.now().strftime("%d-%m-%y_%H_%M_%S")/salida/busquedas.html  "a"------->appending
        fp.write(f'<head>')
        fp.write(f'<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
        fp.write(f'</head>')
        fp.write(r'<style type="text/css"> table {page-break-inside:avoid; width:595px; }')
        fp.write(r".tg {border-collapse:collapse;border-spacing:0;}")
        fp.write(r'.tg td {font-family:TimesNewRoman, Times New Roman;font-size:12px;padding:5px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black}')
        fp.write(r'.tg th {font-family:TimesNewRoman, Times New Roman,:12px;font-weight:normal;padding:5px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}')
        fp.write(r'.tg .tg-rykj {font-size:12px;text-align:left;vertical-align:top}')
        fp.write(r'.tg .tg-0lax {text-align:left;vertical-align:top}')
        fp.write(r'body {height: 842px;width: 595px; margin-left: auto; margin-right: auto;}')
        fp.write(r'.cabe{font-family:TimesNewRoman, Times New Roman;font-size:12px;text-align:right;}')
        fp.write(r'.sintesis {border-style:solid;border-width:1px; border-color:black;text-align:center;font-family:TimesNewRoman, Times New Roman;font-weight: bold; font-size:12px;}')
        fp.write(r'span {font-family:TimesNewRoman, Times New Roman;font-size:12px;margin-left: auto;}')
        fp.write(r'.titulo {font-family:TimesNewRoman, Times New Roman;font-weight: bold; font-size:12px; border-right: 1px solid black;border-bottom:1px solid black;border-top: 1px white; border-left: 1px white;text-align:center;}')
        fp.write(f'</style>')
        fp.write('<body>')
        fp.write('<p class="cabe"> "2020 - A&Ntilde;O DEL GENERAL MANUEL BELGRANO" </p>')
        fp.write('<span>PREFECTURA NAVAL ARGENTINA</span></br>')
        fp.write('<span>AUTORIDAD MARITIMA</font></span></br>')
        fp.write('<span>DIVISION CIBERINTELIGENCIA</span></br>')
        fp.write(f'<p class="sintesis">S&Iacute;NTESIS DE REDES SOCIALES</br>')
        fp.write(f' {fecha_titulo()}</p>')
        fp.close()
    elif event == 'GUARDAR EN REPORTE':                 # se ejecuta cuando ya se ha creado el directorio en el cual se almacenara el reporte
        #director = values[4]
        directorio = values['path'].replace("/salida/busquedas.html", "")       # El "directorio" toma el nuevo valor, con el reporte reescrito con el nuevo reporte agregado a los demás
    busqueda = values[0].strip()                # Remueve los espacios en blanco al inicio y final de "values[0]"
    browser.get(busqueda)                       # The driver.get() method will navigate to a page given by the URL
    time.sleep(6)               # Python time method sleep() suspends execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.

    # CSS selectors are used to select the content you want to style. Selectors are the part of CSS rule set. CSS selectors select HTML elements according to its id, class, type, attribute etc.

    # There are several different types of selectors in CSS.

    # CSS Element Selector
    # CSS Id Selector
    # CSS Class Selector
    # CSS Universal Selector
    # CSS Group Selector
    # "find_element_by_css_selector()" Retorna una lista de elementos web si es que alguno es escontrado. EN caso de que no, retorna una lista vacía

    element= browser.find_element_by_css_selector('div[class="css-1dbjc4n r-1ila09b r-qklmqi r-1adg3ll"]')      # es el HTML de todo el elemento (elemento padre)
    highlight(element)      # Llamada a la función "highlight"
    # break
    autor_url = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]> article > div > div > div.css-1dbjc4n.r-18u37iz.r-thb0q2.r-1mi0q7o > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o > div > div > div > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs > a').get_attribute('href')    # busca y obtiene el HTML correspondiente al autor de la URL (perfil)
    arroba = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]>article > div > div > div.css-1dbjc4n.r-18u37iz.r-thb0q2.r-1mi0q7o > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o > div > div > div > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs > a > div > div.css-1dbjc4n.r-18u37iz.r-1wbh5a2 > div > span').text    # captura el @arroba de la cuenta que publicó
    tweet_cuerpo = (str(texto_tweet3i())).replace(",", "").replace("'", "")     # reemplaza todos las comas (,) y las comillas simples (') por espacios vacíos
    try:
        fecha = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"] > article > div > div > div:nth-child(3) > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep.r-ku1wi2 > div > span:nth-child(1) > span').text      # busca y captura la fecha de la publicación
    except:
        fecha = ''      
    try:
        dispositivo = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]>article > div > div > div:nth-child(3) > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep.r-ku1wi2 > div > a > span').text      # busca y captura el dispositivo desde el cual fue hecha la publicación
    except:
        dispositivo =''
    try:
        interac = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]> article > div > div > div:nth-child(3) > div.css-1dbjc4n.r-1oszu61.r-1kfrmmb.r-1efd50x.r-5kkj8d.r-18u37iz.r-ahm1il.r-a2tzq0').get_attribute('aria-label')   # obtiene las interacciones de la publicación
    except:
        interac = 'sin reacciones'                                       
    try:
        arrobados =  browser.find_elements_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"] div[class="css-901oao r-jwli3a r-1qd0xha r-1blvdjr r-16dba41 r-ad9z0x r-bcqeeo r-19yat4t r-bnwqim r-qvutc0"] > div> span > a')       # arrobados
        arrobados = [x.text for x in arrobados]                 # ciclo que sirve para almacenar los arrobados, en caso de haber más de uno
    except:
        arrobados = ''

    try: 
        link = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]>article > div > div > div:nth-child(3) > div.css-1dbjc4n.r-117bsoe.r-mvpalk.r-156q2ks > div > div > div.css-1dbjc4n.r-1ila09b.r-rull8r.r-qklmqi.r-1adg3ll > a').get_attribute('href')       # obtiene el link de la publicación (atributo href)
    except:
        link = ''

    try:
        link1 = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]>  article > div > div > div:nth-child(3) > div.css-901oao.r-jwli3a.r-1qd0xha.r-1blvdjr.r-16dba41.r-ad9z0x.r-bcqeeo.r-19yat4t.r-bnwqim.r-qvutc0 > a ').get_attribute('title')           # preguntar a que corresponde el link que obtiene en este caso
    except:
        link1 = ' '
    try:
        link3 = browser.find_element_by_css_selector( 'div[style="background: lightgrey; border: 2px solid red;"]> article > div > div > div:nth-child(3) > div:nth-child(1) > div.css-901oao.r-jwli3a.r-1qd0xha.r-1blvdjr.r-16dba41.r-ad9z0x.r-bcqeeo.r-19yat4t.r-bnwqim.r-qvutc0 > a').get_attribute('title')     # preguntar a que corresponde el link que obtiene en este caso
    except:
        link3 =  ' '
    try: 
        ubicacion = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]> article > div > div > div:nth-child(3) > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep.r-ku1wi2 > div > a.css-4rbku5.css-18t94o4.css-901oao.css-16my406.r-1n1174f.r-1loqt21.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-1jeg54m.r-qvutc0 > span').text          # almacena desde donde es twiteado
    except:
        ubicacion = ' '
    nombre_captura3 = (busqueda).replace('/','-').replace(':','-')          # en esta linea se reemplazan las barras (/) y los dos puntos (:) por guiones medios (-)
    nombre_captura3 = os.path.join(directorio + '/salida/screenshots/' + nombre_captura3 + ".png")      # Junta los paths quedando : /Bangho 5/Documents/datetime.datetime.now().strftime("%d-%m-%y_%H_%M_%S")/salida/screenshots/nombre_captura3.png
    tweet_screen = browser.find_element_by_css_selector('div[style="background: lightgrey; border: 2px solid red;"]').screenshot(nombre_captura3)   # toma captura de "nombre_captura3"
    nombre_captura =  (autor_url).replace('/','-').replace(':','-')                         # en esta linea se reemplazan las barras (/) y los dos puntos (:) por guiones medios (-)
    nombre_captura2 = os.path.join(directorio + '/salida/screenshots/usuarios/' + nombre_captura + ".png") # Junta los paths quedando : /Bangho 5/Documents/datetime.datetime.now().strftime("%d-%m-%y_%H_%M_%S")/salida/screenshots/usuarios/nombre_captura.png
    browser.get(autor_url)          # CONSULTAR PARA QUE SE ESTA HACIENDO EL GET ESTE
    time.sleep(6)               # el programa "se duerme" o para su ejecución durante 6 segundos
    try:
        Id = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div').get_attribute('data-testid')
        Id = Id.replace("-follow"," ")
    except:
        Id=''
    try:
        Id1 = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div').get_attribute('data-testid')
        Id1 = Id.replace("-follow"," ")
    except:
        Id1=''
    try: 
        Id3 = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div').get_attribute('data-testid')
        Id3 = Id3.replace("-follow"," ")
    except:
        Id3 = ' '
    cant_tw = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div').text
    try:
        unido = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/span[2]').text
    except:
        unido = '' 
    bio_screen = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[1]').screenshot(nombre_captura2)
    try: 
        adicional = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/span[3]').text
    except:
        adicional = ' '
    with open(os.path.join(directorio +"/salida/busquedas.html"),"a", encoding='utf-8') as fp:  
        titulo = values[1]
        fp.write(f'<p class="titulo">{titulo}</p>')
        fp.write(f'<table class="tg"><tr>')
        fp.write(f'<th class="tg-rykj"><center><b>{busqueda}</b></center></th>')
        fp.write(f'</tr><tr>')
        fp.write(f'<td class="tg-0lax"><center><b>Publicado:</b> {fecha} - {ubicacion} - {dispositivo}</center> </td></tr>')
        nombre_captura3 = nombre_captura3.replace((directorio), '')
        fp.write(f'<tr><td class="tg-0lax">{tweet_cuerpo}')
        fp.write(f'<br><center> <img heigth="275" width="375" src = "''..' + (nombre_captura3) + '" alt ="cfg"> </center>')
        fp.write(f'<br></td></tr>')
        fp.write(f'<tr>')
        fp.write(f'<td class="tg-rykj">')
        fp.write (f"<center>Sobre la cuenta: {arroba} <br> ID: {Id} {Id1} {Id3} - {cant_tw} - {unido} - {adicional} <br></center>")
        nombre_captura2 = nombre_captura2.replace((directorio), '')
        # print(nombre_captura2)
        fp.write( f'<center><img heigth="460" width="330" src = "''..' + (nombre_captura2) + '" alt ="cfg"></center>')
        coment_cuenta = values[2]
        fp.write(f'<center> Impesión general (Vista Rápida) :{coment_cuenta}</center></td></tr>')              
        fp.write(f'<tr><td class="tg-0lax"><center> <b>REPERCUSION</b> </br> ') 
        repercusion = values[3]
        fp.write (f" {interac} -- Arrobados/mencionados: {arrobados}</br>{repercusion}</center></td></tr>")
        fp.write (f"<tr><td><b>Link:</b> {link} </br> {link1} {link3}</center></td></tr>") 
        fp.write ("</table>")

       
        
# from selenium import webdriver
# import time

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('http://codepad.org')

# # click radio button
# python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
# python_button.click()

# # type text
# text_area = driver.find_element_by_id('textarea')
# text_area.send_keys("print('Hello World')")

# # click submit button
# submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
# submit_button.click()