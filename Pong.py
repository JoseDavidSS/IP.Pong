import pygame
from pygame.locals import *
from tkinter import *

# Clase del juego e interaz
class Juego:
    # Atributos
    def __init__(self, matriz):
        self.matriz = matriz
    # Sets y Gets
    def getMatriz(self):
        return self.matriz
    # Métodos
    def menu_principal(self):
        ventana = Tk()
        ventana.title("Menu Principal")
        ventana.minsize(1080, 720)
        ventana.resizable(width=NO, height=NO)

        # Crear Canvas
        canvas = Canvas(ventana, width=1080, height=720, bg="#40FF00")
        canvas.place(x=-2, y=-2)
        canvas.pack()

        ventana.mainloop()  # Final del programa
Instancia_Juego = Juego("matriz")
Instancia_Juego. menu_principal()

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

