from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import urllib.parse
from bs4 import BeautifulSoup

HOST_NAME="https://transparencia.gob.es"
NUM_MAXIMO_PAGINAS=1000
NOMBRE_FICHERO_DATOS="datos.csv"

def escribir_fichero_debug(texto):
    with open("salida.html","w",encoding="UTF-8") as fichero:
        fichero.write(texto)

def escribir_fichero(*datos):
    with open(NOMBRE_FICHERO_DATOS,"a",encoding="UTF-8") as fichero:
        for dato in datos:
            fichero.write(dato)
            fichero.write("\t")
        fichero.write("\n")

def procesar_detalle(url):
    try:
        url = url.replace(" ","%20")
        html=urlopen(url)
    except HTTPError:
        print("Ha ocurrido un error HTTP")
    except URLError:
        print("Ha ocurrido un error URL")
    else:
        codigo_html = html.read()
        html_limpio = BeautifulSoup(codigo_html, 'html.parser')
        try:
            h3_adjudicatario = html_limpio.find("h3", string="Adjudicatario:")
            adjudicatario = h3_adjudicatario.nextSibling.nextSibling.text
        except:
            adjudicatario="¿Desierto?"
    return adjudicatario

def procesar_html(codigo_html):
    html_limpio = BeautifulSoup(codigo_html, 'html.parser')
    tabla_resultados = html_limpio.find(id="resultados")
    #escribir_fichero_debug(str(tabla_resultados))
    
    tbody=tabla_resultados.find("tbody")
    #escribir_fichero_debug(str(tbody))
    trs = tbody.findAll("tr")
    for tr in trs:
        titulo = tr.find(id="tituloColumna").a.text.strip()
        enlace_detalle = HOST_NAME + tr.find(id="tituloColumna").a.attrs['href']
        adjudicatario = procesar_detalle(enlace_detalle)
        ministerio = tr.find(id="ministerioColumna").text.strip()
        organo = tr.find(id="organoContratacionColumna").text.strip()
        procedimiento = tr.find(id="procedimientoContratacionColumna").text.strip()
        fecha = tr.find(id="fechaAdjudicacionColumna").text.strip()
        importe = tr.find(id="importeAdjudicacionColumna").text.strip()
        escribir_fichero(titulo, ministerio, organo, procedimiento, fecha, importe, adjudicatario)
    enlace_siguiente = html_limpio.find("a", string="Siguiente")
    enlace_siguiente = HOST_NAME + enlace_siguiente.attrs['href']
    return enlace_siguiente

url = "https://transparencia.gob.es/servicios-buscador/buscar.htm?"\
        "pag=1&categoria=licitaciones&categoriasPadre=conconvsub&ente=E05025101"\
        ",E05071301&historico=false&lang=es"
numero_paginas = 0
while(True):
    try:
        html=urlopen(url)
    except HTTPError:
        print("Ha ocurrido un error HTTP")
    except URLError:
        print("Ha ocurrido un error URL")
    else:
        print("1")
        codigo_html = html.read()
        print("2")
        url = procesar_html(codigo_html=codigo_html)
        print("3")
        print(url)
        numero_paginas+=1
        if (numero_paginas>NUM_MAXIMO_PAGINAS):
            break