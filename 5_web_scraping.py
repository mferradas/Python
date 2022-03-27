'''
Enunciado:
- Obtener todas las películas y series
- Obtener la metadata de cada contenido: título, año, sinopsis, link, duración (solo para movies)
- Guardar la información obtenida en una base de datos, en archivo .json o .csv automáticamente
    PLUS: Episodios de cada serie
    PLUS: Metadata de los episodios
    PLUS: Si es posible obtener mas información/metadata por cada contenido
    PLUS: Identificar modelo de negocio
    
    Fecha límite para entrega: lunes 21 de febrero a las 11:00hs.
- Sitio a realizar el scraping:https://www.starz.com/ar
- Requisitos:
    
    Tenes la libertad de utilizar la librería que quieras para realizarlo.
    
    Subir a GitHub el script trabajado junto con un archivo de los resultados que se obtienen al correr el script creado (JSON, xlsx, csv, etc)
'''
#trabajaremos con la librería 'Selenium'
from selenium import webdriver
#Esto espera a que cargue el UI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#trabajaremos con 'Pandas' para hacer la exportación de datos a '.csv'
import pandas as pd

# Opciones de navegación:
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized') #el navegador iniciará maximizado por defecto
options.add_argument('--disable-extensions') #deshabilitamos las extensiones para asegurar la compatibilidad con 'Chromedriver'

driver_path = 'C:\\chromedriver.exe' #indicamos el path en donde se encontrará alojado 'Chromedriver'

driver = webdriver.Chrome(driver_path, chrome_options=options) #asociamos 'Chromedriver' con el path definido y las opciones por defecto que declaramos anteriormente

# Iniciar en la pantalla '2' (borrar este bloque si no contamos con 2 monitores)
driver.set_window_position(-2000, 0)
driver.maximize_window()
time.sleep(1)


#inicializamos el navegador
driver.get('https://www.starz.com/ar/es/')

#accedemos al link de 'Series'
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      ' //*[@id="view-container"]/starz-header/header/div/div/div[1]/a[2]')))\
    .click()

#el browser scrollea la pantalla para cargar todas las series
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.4);")


#creamos un array vacio para almacenar las series
list_series = []
time.sleep(2)    
#agregará cada elemento 'h6' encontrado dentro del array 'list_series'
series = driver.find_elements(By.TAG_NAME, 'h6')
for s in series: #ejecutamos la iteración de los elementos encontrados...
    list_series.append(s.text) #...y los guardamos en la lista 'list_series' en formato 'texto'

#eliminamos los campos vacíos que pudieran encontrarse dentro del array
list_series = filter(None, list_series)

#imprimimos el resultado del array 'list_series' (aunque no es necesario)
print(list_series)

#usamos 'Panda' para guardar la información obtenida en un archivo '.csv' (es recomendable porque usa poca memoria)
pd.DataFrame(list_series).to_csv("Datos/Series.csv")

#hasta aquí, se han guardado todas las series en un archivo '.csv' externo
#a continuación, comenzaremos con las películas:

#accedemos al link de 'Películas'
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="view-container"]/starz-header/header/div/div/div[1]/a[3]')))\
    .click()

#el browser scrollea la pantalla para cargar todas las películas
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.4);")

#creamos un array vacio para almacenar las películas
list_metadata = []
time.sleep(2)    
#por cada elemento 'metadata' que encuentre...
metadatap = driver.find_elements(By.CLASS_NAME, 'metadata-container')
for m in metadatap:
    list_metadata.append(m.text) #almacenará los mismos, una vez iterados, dentro de la lista 'list_metadata'

#imprimimos el resultado del array 'list_metadata' (aunque no es necesario)
print(list_metadata)

#eliminamos los campos vacíos que pudieran encontrarse dentro del array
list_metadata = filter(None, list_metadata)

#nuevamente, usamos 'Pandas' para guardar la información en un archivo '.csv'
pd.DataFrame(list_metadata).to_csv("Datos/Peliculas.csv")