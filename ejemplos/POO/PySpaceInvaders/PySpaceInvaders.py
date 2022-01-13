import pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import sys

#Inicialización de el entorno
pygame.init()
#Game config
windowWidth = 640
windowHeight = 400
window = pygame.display.set_mode((windowWidth, windowHeight))
NUMERO_ENEMIGOS = 6

#Reloj del juego
reloj = pygame.time.Clock()

#Tiempo inicial del juego
startTick = pygame.time.get_ticks()

class Enemigo:
    x_speed = 2
    y_speed = 10
    y = 10

    def __init__(self, sprite, x, width, height):
        self.sprite = pygame.image.load(sprite)
        self.x = x
        self.width = width
        self.height = height
        self.sprite = pygame.transform.scale(self.sprite, (width, height))

    def actuar(self):
        self.__mover()
        self.__dibujar()

    def __mover(self):
        self.x += Enemigo.x_speed
        if (self.x>=windowWidth-self.width):
            Enemigo.y += Enemigo.y_speed
            Enemigo.x_speed = Enemigo.x_speed * -1
        elif (self.x<=0):
            Enemigo.y += Enemigo.y_speed
            Enemigo.x_speed = Enemigo.x_speed * -1
            self.x += Enemigo.x_speed*2 #Corregimos las posición del primer enemigo de la lista

    def __dibujar(self):
        window.blit(self.sprite, (self.x, Enemigo.y))  # Dibujar al enemigo


enemigos = []
for i in range(0,NUMERO_ENEMIGOS):
    x = 10 + (60 * i)
    enemigos.append(Enemigo("sprites/enemy1.png", x, 50, 50))

#Game Loop
while True:
    # Ritmo del juego
    reloj.tick(60)
    # Background color - Clear window
    window.fill((0, 0, 0))#Pintar el fondo de la ventana

    for enemigo in enemigos:
        enemigo.actuar()

    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                pass
    pygame.display.update()
