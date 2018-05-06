import pygame
from pygame.locals import *
from tkinter import *
ventana = Tk()
ventana.withdraw()
# Clase del juego e interaz

class Juego:
    # Atributos
    def __init__(self):
        self.matriz = hacer_matriz(25, 40)
    # Sets y Gets
    def getMatriz(self):
        return self.matriz
    # Métodos
    def menu_principal(self):
        ventana.deiconify()
        ventana.title("PONG")
        ventana.minsize(1080, 720)
        ventana.resizable(width = NO, height = NO)

        # Crear Canvas
        canvas = Canvas(ventana, width = 1080, height = 720, bg = "black")
        canvas.place(x=-2, y=-2)
        canvas.pack()

        #Labels
        titulo = Label(ventana, text = "PONG", font = ("IMPACT", "20"), bg = "black", fg = "white")
        titulo.place(x = 494, y = 10)

        button = Button(ventana, text = "pr", command = self.entrar)
        button.place(x = 100, y = 100)

        ventana.mainloop()  # Final del programa
    def pantalla_juego(self):
        color_pantalla = (10, 10, 10)
        pygame.init()
        pantalla = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("PONG")
        pantalla.fill(color_pantalla)
        bola = Bola((50,50), 5, 0)
        pygame.display.update()
        while True:
            bola.crearbola(pantalla)
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    def entrar(self):
        ventana.withdraw()
        Instancia_Juego.pantalla_juego()

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
    def golpea_ultimo(self):
        if not equipo:
            bola.setUltimo_Golpe(0)
        else:
            bola.setUltimo_Golpe(1)

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
    def crearbola(self, superficie):
        pygame.draw.circle(superficie, (249, 249, 249), posicion, 10)

Instancia_Juego = Juego()
Instancia_Juego.menu_principal()

