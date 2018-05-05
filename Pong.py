import pygame
from pygame.locals import *
from tkinter import *

class Barras:
    def __init__(self, largo, direccion_sobrebola, cpu, posicion, puntos, velocidad):
        self.largo = largo
        self.direccion_sobrebola = direccion_sobrebola
        self.cpu = cpu
        self.posicion = posicion
        self.puntos = puntos
        self.velocidad = velocidad
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

class Bola:
    def __init__(self, posicion, velocidad, ultimo_golpe):
        self.posicion = posicion
        self.velocidad = velocidad
        self.ultimo_golpe = ultimo_golpe
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

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("PONG")

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()