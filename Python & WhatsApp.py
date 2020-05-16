'''
Utilizando Python para automatizar un reporte de productos FOCO para enviar a los CTNs
'''
class datos:
    def __init__(self):
        self.usuario = "usuario"
        self.password = "contraseña"
        self.url = "URL del login de Power BI"
        self.urli = "URL del informe de Power BI"
        self.chrome_path = r"local del chromedriver.exe"

import time
import autopy
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


datos = datos()

#declarando variables
login = datos.usuario
passw = datos.password
chrome_path = datos.chrome_path
url01 = datos.url
url02 = datos.urli

#ejecutando webdriver y abriendo el sitio web de power bi
driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get(url01)


#Pasando el usuario
time.sleep(5)
element = driver.find_element_by_id("i0116")
element.send_keys(login)
driver.find_element_by_id("idSIButton9").click()

#Pasando la contraseña
time.sleep(5)
element = driver.find_element_by_id("i0118")
element.send_keys(passw)
driver.find_element_by_id("idSIButton9").submit()

#confirmando acceso
time.sleep(5)
driver.find_element_by_id("idSIButton9").submit()

#Redireccionando la página al informe de productos foco (Todos los CTNs)
time.sleep(10)
driver.get(url02)

#Sacando captura de pantalla y guardando como imagen .png (Todos CTNs)
time.sleep(30)
screenshot = autopy.bitmap.capture_screen(((200, 280), (900, 435)))
screenshot.save("Todos_CTNs.png")


#Cargando la página web de WhatSapp
driver = webdriver.Chrome(chrome_path)
driver.get('https://web.whatsapp.com/')

#Declarando la ubicación de la imagen a adjuntar
filepath = r"local de imagen"

#Pasando el nombre del contacto o grupo para enviar la imagen
time.sleep(10)
user = driver.find_element_by_xpath('//span[@title = "nombre contacto"]')
user.click()

#Adjuntando archivo para enviar al contacto seleccionado.
attachment_box = driver.find_element_by_xpath('//div[@title = "Adjuntar"]')
attachment_box.click()

#incluyendo la variable del local path de la imagen que enviaré en adjunto
image_box = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

#click en enviar la imagen
time.sleep(3)
send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()

time.sleep(150)