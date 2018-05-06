import pygame
from pygame.locals import *

class Juego:
    def __init__(self):
        self.matriz = hacer_matriz(25, 40)
    def getMatriz(self):
        return self.matriz
    def setMatriz(self, nuevo):
        self.matriz = nuevo

class Bola:
    def __init__(self):
        self.posicion = (540, 360)
        self.velocidad = 3
        self.ultimo_golpe = 0
    def getPosicion(self):
        return self.posicion
    def getVelocidad(self):
        return self.velocidad
    def getUltimo_golpe(self):
        return self.ultimo_golpe
    def setPosicion(self, nuevo):
        self.posicion = nuevo
    def setVelocidad(self, nuevo):
        self.velocidad = nuevo
    def setUltimo_Golpe(self, nuevo):
        self.ultimo_golpe = nuevo
    def crearbola(self, superficie):
        pygame.draw.circle(superficie, (249, 249, 249), (540, 360), 10)

class Barras:
    def __init__(self, largo, direccion_sobrebola, cpu, posicion, puntos, velocidad, equipo):
        self.largo = largo
        self.direccion_sobrebola = direccion_sobrebola
        self.cpu = cpu
        self.posicion = posicion
        self.puntos = puntos
        self.velocidad = velocidad
        self.equipo = equipo
    def getLargo(self):
        return self.largo
    def getDireccion(self):
        return self.direccion_sobrebola
    def getPosicion(self):
        return self.posicion
    def getPuntos(self):
        return self.puntos
    def getVelocidad(self):
        return self.velocidad
    def setPosicion(self, nuevo):
        self.posicion = nuevo
    def setPuntos(self, nuevo):
        self.puntos = nuevo
    def setVelocidad(self, nuevo):
        self.velocidad = nuevo

def hacer_matriz(filas, columnas):
    M = []
    subM = []
    n = 0
    m = 0
    while n < filas:
        while m < columnas:
            subM.append(0)
            m += 1
        m = 0
        M.append(subM)
        subM = []
        n += 1
    return M


pygame.init()
pantalla = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("PONG")
pantalla.fill((10, 10, 10))
bola = Bola()
while True:
    bola.crearbola(pantalla)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()