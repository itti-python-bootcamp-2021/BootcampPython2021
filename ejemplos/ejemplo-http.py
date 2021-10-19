import http.client
conn = http.client.HTTPSConnection("fpaniaguaformacion.github.io")
conn.request("GET", "/")
r1 = conn.getresponse()
data1 = r1.read()
print(data1)
conn.close()