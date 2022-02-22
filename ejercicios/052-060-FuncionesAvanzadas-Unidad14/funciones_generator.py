"""
El WebService "fake" genera pronósticos del tiempo que tardan 1 segundo en generarse
El "generator" get_pronosticos invoca al "WebService" secuencialmente para obtener
hasta 1.000.000 de pronósticos.
"""
from time import sleep
from random import randrange

class WebService:
    def get_pronostico(self):
        sleep(1)
        print("Generando pronóstico...")
        return randrange(-5,40)

def get_pronosticos():
    ws = WebService()
    for i in range(1_000_000):
        yield ws.get_pronostico()

for pronostico in get_pronosticos():
    print("Procesando pronostico",pronostico)




