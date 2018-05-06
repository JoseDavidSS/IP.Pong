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

        # Crear Ventana
        ventana = Tk()
        ventana.title("Menu Principal")
        ventana.minsize(1080, 720)
        ventana.resizable(width=NO, height=NO)

        # Crear Canvas
        canvas = Canvas(ventana, width=1080, height=720, bg="#40FF00")
        canvas.place(x=-2, y=-2)
        canvas.pack()

        def ventana2():
            ventana.destroy()
            Instancia_Juego.ventana_juego()

        # Boton animacion
        Juego_boton = Button(canvas,
                                 text="Jugar",
                                 font=("Arial", 20),
                                 width=10,
                                 bg="yellow",
                                 command = ventana2)
        Juego_boton.place(x=800, y=600)

        # Fin del loop
        ventana.mainloop()

    def ventana_juego(self):
        ColorUno = (0, 140, 60)
        ColorDos = pygame.Color(255, 120, 9)
        pygame.init()
        ventana = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Hola Mundo")
        clock = pygame.time.Clock()

        crashed = False
        while not crashed:
            ventana.fill(ColorDos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                print(event)
            pygame.display.update()
            clock.tick(60)

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
