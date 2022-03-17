import requests
import json
from django.http import HttpResponse

respuesta = requests.get('http://localhost:8000/api/videojuego/')

json_array = json.loads(respuesta.content)
for json_object in json_array:
    print(json_object["id"], json_object["titulo"])