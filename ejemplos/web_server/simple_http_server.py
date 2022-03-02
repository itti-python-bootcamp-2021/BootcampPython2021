from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from gestor_usuarios import Usuario
import json

hostName = "localhost"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path=="/"):
            self.send_response(200)#OK
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("registro.html","r",encoding="UTF-8") as formulario_html:
                html = formulario_html.read()
                print(html)
                self.wfile.write(bytes(html,"utf-8"))
                self.wfile.flush()
        elif ("?" in self.path):
            accion, parametros = self.path.split("?")
            datos_url = urlparse(parametros)
            if (accion=="/registro"):
                parametros_url = parse_qs(datos_url.path) # Diccionario clave:lista
                correo = parametros_url["correo"][0]
                pwd = parametros_url["pwd"][0]
                #En este punto tenemos correo y pwd.
                #Inicio de la ejecución de la lógica de la operación
                nuevoUsuario = Usuario(correo, pwd)
                nuevoUsuario.store()    
                #Fin de la ejecución de la lógica de la operación
                #Inicio de la generación de la salida
                self.send_response(200)#OK
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>My App</title></head>", "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes(f"<h1>El usuario {correo} se ha registrado correctamente</h1>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
                self.wfile.flush()
                #Fin de la generación de la salida
            elif (accion=="/validacion"):
                pass
            """
            parametros_url = parse_qs(datos_url.query) # Diccionario clave:lista
            nombre="desconocido"
            if ("nombre" in parametros_url.keys()):
                nombre = parametros_url["nombre"][0]

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>My Python Web Server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<h1>Python Web Server</h1>", "utf-8"))
            self.wfile.write(bytes(f"<h2>Hola {nombre}</h2>", "utf-8"))
            self.wfile.write(bytes(f"<p>Request: {self.path}", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
            """
    def do_POST(self):
        datos_url = urlparse(self.path)
        parametros_url = parse_qs(datos_url.query) # Diccionario clave:lista
        nombre="desconocido"
        if ("nombre" in parametros_url.keys()):
            nombre = parametros_url["nombre"][0]
        datos =  {"nombre":nombre, "edad":50, "ciudad":"Alcorcón"}
        datos_json = json.dumps(datos)
        print(datos_json)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(datos_json,"utf-8"))















if __name__ == "__main__":        
    web_server = HTTPServer((hostName, serverPort), MyServer)
    print(f"Servidor arrancado en {hostName}:{serverPort}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Servidor detenido.")


"""
from urlparse import urlparse, parse_qs
query_components = parse_qs(urlparse(self.path).query)
imsi = query_components["imsi"] 
"""
