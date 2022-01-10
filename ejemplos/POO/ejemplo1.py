"""
Tenemos 12x5 enemigos. 60.
Los enemigos se mueven de izquierda a derecha hasta que el enemigo del extremo derecho llega al borde-->
desciende 5 pixeles --> Comienzan a moverse de derecha a izquierda
Cada cierto tiempo uno de los enemigos dispara


Tenemos una nave espacial que dispara (player)
Podemos moverlo
Podemos disparar

Si un disparo enemigo impacta en el player lo destruye.
Si un disparo del player impactaen el enemigo lo destruye.
"""
import time
class Enemigo:
    #ATRIBUTOS ESTÁTICOS O DE CLASE
    DISTANCIA_X=50
    velocidad_x = 1
    velocidad_y = 1
    y = 0
    #CONSTRUCTOR
    def __init__(self, x, fichero_sprite):
        #ATRIBUTOS NO ESTÁTICOS O DE INSTANCIA
        self.x = x
        self.vivo = True
        #leer el sprite
        self.sprite = None
    #MÉTODOS
    def mover_horizontal(self):
        self.x+=Enemigo.velocidad_x
        if (self.x>=205 or self.x<=0):
            Enemigo.velocidad_x*=-1
            self.mover_vertical()
    def mover_vertical(self):
        Enemigo.y+=Enemigo.velocidad_y
    def disparar(self):
        print("Disparando...")
    def morir(self):
        print("Muriendo...")
    def draw(self, lienzo):
        print("Dibujando...")

enemigos=[]

#0,50,100,150,200
for i in range(0,5):
    enemigos.append(Enemigo(i*Enemigo.DISTANCIA_X,"EnemigoTipo1.png"))

while (True):
    for enemigo in enemigos:
        enemigo.mover_horizontal()
        enemigo.draw(None)
    time.sleep(0.1)