import requests
import json

api_url = 'http://localhost:8080?nombre=Harris'
api_url_get = 'http://localhost:8080'
api_url_post = 'http://localhost:8080'
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

print(do_get_request(api_url_get))


def do_post_request(api_url):
    response = requests.post(api_url, params={'nombre': 'Harrison Ford'})
    status_code = response.status_code
    print(status_code)
    json_response={}
    if (status_code==200):
        json_response = json.loads(response.text)
    return json_response

print(do_post_request(api_url_post))