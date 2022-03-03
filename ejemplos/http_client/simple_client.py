import requests
import json

#api_url = 'http://localhost:8080?nombre=Harris'
api_url_get = 'http://localhost:8080'
api_url_post = 'http://localhost:80'
#api_url = 'https://elpais.com/paginaprincipal/' #Provoca 404 y 403

def do_get_request(api_url):
    response = requests.get(api_url, params={'nombre': 'Harrison Ford'})
    print(response)
    status_code = response.status_code
    print(status_code)
    html_response="None"
    if (status_code==200):
        html_response = response.text
    return html_response

#print(do_get_request(api_url_get))


def do_post_request(api_post_url):
    respuesta = requests.post(api_post_url, params={'pais': 'Kenia'})
    status_code = respuesta.status_code
    print(status_code)
    json_response={}
    if (status_code==200):
        json_response = json.loads(respuesta.text)
    return json_response

#print(do_post_request('http://localhost:80'))

def get_info_pelicula(titulo):
    #http://www.omdbapi.com/?apikey=ee6e8770&s=Tron
    respuesta = requests.get("http://www.omdbapi.com/", params={'apikey': 'ee6e8770', "s" : titulo})
    status_code = respuesta.status_code
    #print(status_code)
    json_response={}
    if (status_code==200):
        json_response = json.loads(respuesta.text)
    return json_response

def get_peli(imdbID):
    respuesta = requests.get("http://www.omdbapi.com/", params={'apikey': 'ee6e8770', "i" : imdbID})
    status_code = respuesta.status_code
    #print(status_code)
    json_response={}
    if (status_code==200):
        json_response = json.loads(respuesta.text)
    return json_response

lista_peliculas = get_info_pelicula("Star Trek")["Search"]
for peli in lista_peliculas:
    imdbID = peli["imdbID"]
    peli = get_peli(imdbID)
    print(peli["Title"],peli["Director"],peli["Year"])
    