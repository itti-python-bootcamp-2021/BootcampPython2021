import requests

x = requests.delete('http://localhost:8000/api/videojuego/2/')

print(x.text)