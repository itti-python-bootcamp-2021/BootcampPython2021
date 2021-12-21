import json

#paises = {"Francia":"París","Alemania":"Berlín","Portugal":"Lisboa","Bulgaria":"Sofia"}

paises = {"Europa":{"Francia":"París","Alemania":"Berlín","Portugal":"Lisboa","Bulgaria":"Sofia"},
         "América":{"Argentina":"Buenos Aires","Uruguay":"Montevideo","Brasil":"Brasilia"}}


with open("paises.json","w",encoding="UTF-8") as fichero:
    fichero.write(json.dumps(paises))
