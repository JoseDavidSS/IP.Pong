import pygame as pygame
import time
from tkinter import *
import random

pantalla = []

cerrar = True

filas = 25
columnas = 40

largo_pantalla = 1080
ancho_pantalla = 720

largo_cuadro = largo_pantalla // columnas
ancho_cuadro = ancho_pantalla // filas

negro = (0, 0, 0)
blanco = (255, 255, 255)

nivel = 1
barras = 1

reloj = pygame.time.Clock()
Fps = 20

comprobar = 0

pygame.init()

class Juego:
    def __init__(self, M):
        self.M = M
        for n in range(filas):
            self.M.append([])
            for m in range(columnas):
                self.M[n].append(0)
    def hacer_matriz(self):
        if barras == 1:
            if nivel == 1:
                for n in range(filas):
                    for m in range(columnas):
                        if n >= 7 and n <= 9 and m == 2:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 2:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 2:
                            self.M[n][m] = 13
                        elif n >= 7 and n <= 15 and m == 37:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 37:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 37:
                            self.M[n][m] = 13
                        elif n == 11 and m == 19:
                            self.M[n][m] = 2
                        elif n == 0:
                            self.M[n][m] = 31
                        elif n == 24:
                            self.M[n][m] = 32
                        elif m == 0:
                            self.M[n][m] = 41
                        elif m == 39:
                            self.M[n][m] = 42
                        else:
                            self.M[n][m] = 0
            elif nivel == 2:
                for n in range(filas):
                    for m in range(columnas):
                        if n >= 11 and n <= 12 and m == 2:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 2:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 2:
                            self.M[n][m] = 13
                        elif n >= 11 and n <= 12 and m == 37:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 37:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 37:
                            self.M[n][m] = 13
                        elif n == 11 and m == 19:
                            self.M[n][m] = 2
                        elif n == 0:
                            self.M[n][m] = 31
                        elif n == 24:
                            self.M[n][m] = 32
                        elif m == 0:
                            self.M[n][m] = 41
                        elif m == 39:
                            self.M[n][m] = 42
                        else:
                            self.M[n][m] = 0
            else:
                for n in range(filas):
                    for m in range(columnas):
                        if n == 11 and m == 2:
                            self.M[n][m] = 11
                        elif n == 12 and m == 2:
                            self.M[n][m] = 12
                        elif n == 13 and m == 2:
                            self.M[n][m] = 13
                        elif n == 11 and m == 37:
                            self.M[n][m] = 11
                        elif n == 12 and m == 37:
                            self.M[n][m] = 12
                        elif n == 13 and m == 37:
                            self.M[n][m] = 13
                        elif n == 11 and m == 19:
                            self.M[n][m] = 2
                        elif n == 0:
                            self.M[n][m] = 31
                        elif n == 24:
                            self.M[n][m] = 32
                        elif m == 0:
                            self.M[n][m] = 41
                        elif m == 39:
                            self.M[n][m] = 42
                        else:
                            self.M[n][m] = 0
        else:
            if nivel == 1:
                for n in range(filas):
                    for m in range(columnas):
                        if n >= 7 and n <= 9 and m == 2:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 2:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 2:
                            self.M[n][m] = 13
                        elif n >= 7 and n <= 9 and m == 6:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 6:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 6:
                            self.M[n][m] = 13
                        elif n >= 7 and n <= 15 and m == 37:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 37:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 37:
                            self.M[n][m] = 13
                        elif n >= 7 and n <= 15 and m == 33:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 33:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 33:
                            self.M[n][m] = 13
                        elif n == 11 and m == 19:
                            self.M[n][m] = 2
                        elif n == 0:
                            self.M[n][m] = 31
                        elif n == 24:
                            self.M[n][m] = 32
                        elif m == 0:
                            self.M[n][m] = 41
                        elif m == 39:
                            self.M[n][m] = 42
                        else:
                            self.M[n][m] = 0
            elif nivel == 2:
                for n in range(filas):
                    for m in range(columnas):
                        if n >= 11 and n <= 12 and m == 2:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 2:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 2:
                            self.M[n][m] = 13
                        elif n >= 11 and n <= 12 and m == 6:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 6:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 6:
                            self.M[n][m] = 13
                        elif n >= 11 and n <= 12 and m == 37:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 37:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 37:
                            self.M[n][m] = 13
                        elif n >= 11 and n <= 12 and m == 33:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 33:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 33:
                            self.M[n][m] = 13
                        elif n == 11 and m == 19:
                            self.M[n][m] = 2
                        elif n == 0:
                            self.M[n][m] = 31
                        elif n == 24:
                            self.M[n][m] = 32
                        elif m == 0:
                            self.M[n][m] = 41
                        elif m == 39:
                            self.M[n][m] = 42
                        else:
                            self.M[n][m] = 0
            else:
                for n in range(filas):
                    for m in range(columnas):
                        if n == 11 and m == 2:
                            self.M[n][m] = 11
                        elif n == 12 and m == 2:
                            self.M[n][m] = 12
                        elif n == 13 and m == 2:
                            self.M[n][m] = 13
                        elif n == 11 and m == 6:
                            self.M[n][m] = 11
                        elif n == 12 and m == 6:
                            self.M[n][m] = 12
                        elif n == 13 and m == 6:
                            self.M[n][m] = 13
                        elif n == 11 and m == 37:
                            self.M[n][m] = 11
                        elif n == 12 and m == 37:
                            self.M[n][m] = 12
                        elif n == 13 and m == 37:
                            self.M[n][m] = 13
                        elif n == 11 and m == 33:
                            self.M[n][m] = 11
                        elif n == 12 and m == 33:
                            self.M[n][m] = 12
                        elif n == 13 and m == 33:
                            self.M[n][m] = 13
                        elif n == 11 and m == 19:
                            self.M[n][m] = 2
                        elif n == 0:
                            self.M[n][m] = 31
                        elif n == 24:
                            self.M[n][m] = 32
                        elif m == 0:
                            self.M[n][m] = 41
                        elif m == 39:
                            self.M[n][m] = 42
                        else:
                            self.M[n][m] = 0
    def getMatriz(self):
        return self.M
    def setMatriz(self, nuevo):
        self.M = nuevo
    def menu_principal(self):
        # Crear Ventana
        ventana = Tk()
        ventana.title("Menu Principal")
        ventana.minsize(1080, 720)
        ventana.resizable(width=NO, height=NO)

        # Crear Canvas
        canvas = Canvas(ventana, width=1080, height=720, bg="black")
        canvas.place(x=-2, y=-2)
        canvas.pack()

        # Funciones que llaman a los otros métodos de la clase con instancias
        def ventana_un_jugador_aux():
            ventana.destroy()
            juego.ventana_un_jugador()

        def ventana_dos_jugadores_aux():
            ventana.withdraw()
            juego.ventana_dos_jugadores()

        def ventana_instrucciones_aux():
            ventana.withdraw()
            juego.ventana_instrucciones()

        # Boton para iniciar partida de un jugador
        un_jugador = Button(canvas,
                            text="Un jugador",
                            font=("Arial", 20),
                            width=14,
                            bg="white",
                            command=ventana_un_jugador_aux)
        un_jugador.place(x=425, y=300)

        # Boton para iniciar partida de dos jugadores
        dos_jugadores = Button(canvas,
                               text="Dos Jugadores",
                               font=("Arial", 20),
                               width=14,
                               bg="white",
                               command=ventana_dos_jugadores_aux)
        dos_jugadores.place(x=425, y=400)

        # Boton para ir a ventana de instrucciones
        bt_instrucciones = Button(canvas,
                                  text="Instrucciones",
                                  font=("Arial", 20),
                                  width=14,
                                  bg="white",
                                  command=ventana_instrucciones_aux)
        bt_instrucciones.place(x=425, y=600)

        # Labels
        titulo = Label(canvas,
                       text="PONG",
                       font=("Arial", 78),
                       bg="black",
                       fg="white")
        titulo.place(x=390, y=15)

        # Fin del loop
        ventana.mainloop()

    def ventana_un_jugador(self):
        global cerrar
        barra2.setCPU(1)
        cerrar = False

    def ventana_dos_jugadores(self):
        # Crear Ventana
        ventana_dos_jugadores = Tk()
        ventana_dos_jugadores.title("Dos Jugadores")
        ventana_dos_jugadores.minsize(1080, 720)
        ventana_dos_jugadores.resizable(width=NO, height=NO)

        # Crear Canvas
        canvas_dos_jugadores = Canvas(ventana_dos_jugadores, width=1080, height=720, bg="black")
        canvas_dos_jugadores.place(x=-2, y=-2)
        canvas_dos_jugadores.pack()

        def volver():
            ventana_dos_jugadores.destroy()
            juego.menu_principal()

        def modo_singles_aux():
            ventana_dos_jugadores.destroy()
            juego.modo_singles()

        def modo_doubles_aux():
            ventana_dos_jugadores.destroy()
            juego.modo_doubles()

        # Botón para volver al menú principal
        atras = Button(canvas_dos_jugadores,
                       text="Volver al Menú Principal",
                       font=("Arial", 16),
                       bg="white",
                       command=volver)
        atras.place(x=820, y=25)

        # Botón para jugar modo singles
        singles = Button(canvas_dos_jugadores,
                         text="Jugar modo Singles",
                         font=("Arial", 20),
                         bg="white",
                         command=modo_singles_aux)
        singles.place(x=420, y=300)

        # Botón para jugar modo doubles
        doubles = Button(canvas_dos_jugadores,
                         text="Jugar modo Doubles",
                         font=("Arial", 20),
                         bg="white",
                         command=modo_doubles_aux)
        doubles.place(x=420, y=600)

        # Labels de descripciones de modos de juego
        descripcion_singles = Label(canvas_dos_jugadores,
                                    text="Modo Singles es un un tipo de juego en el que participan\n dos jugadores, y cada jugador controla una paleta",
                                    font=("Arial", 20),
                                    bg="black",
                                    fg="white")
        descripcion_singles.place(x=200, y=200)

        descripcion_doubles = Label(canvas_dos_jugadores,
                                    text="Modo Doubles: a diferencia del Modo Singles, este es un un tipo de juego\n en el que participan dos jugadores, y cada jugador controla dos paletas",
                                    font=("Arial", 20),
                                    bg="black",
                                    fg="white")
        descripcion_doubles.place(x=95, y=500)

    def modo_singles(self):
        global cerrar
        juego.hacer_matriz()
        cerrar = False

    def modo_doubles(self):
        global cerrar
        global barras
        barras = 2
        juego.hacer_matriz()
        cerrar = False


    def ventana_instrucciones(self):
        # Crear Ventana
        ventana_instrucciones = Tk()
        ventana_instrucciones.title("Intrucciones")
        ventana_instrucciones.minsize(1080, 720)
        ventana_instrucciones.resizable(width=NO, height=NO)

        # Crear Canvas
        canvas_instrucciones = Canvas(ventana_instrucciones, width=1080, height=720, bg="black")
        canvas_instrucciones.place(x=-2, y=-2)
        canvas_instrucciones.pack()

        def volver():
            ventana_instrucciones.destroy()
            juego.menu_principal()

        # Botón para volver al menú principal
        atras = Button(canvas_instrucciones,
                       text="Volver al Menú Principal",
                       font=("Arial", 16),
                       bg="white",
                       command=volver)
        atras.place(x=820, y=25)

        # Labels de descripcion de Juego y sus Controles
        descripcion_juego = Label(canvas_instrucciones,
                                  text="Descripción: \n \n"
                                       "Pong es un juego de deportes en dos dimensiones que simula un tenis de mesa. \n"
                                       "El jugador controla en el juego una paleta moviéndola verticalmente en la parte izquierda de la pantalla,\n"
                                       "y puede competir tanto contra un oponente controlado por computadora, como con otro jugador\n"
                                       "humano que controla una segunda paleta en la parte opuesta. Los jugadores pueden usar las paletas\n"
                                       "para pegarle a la pelota hacia un lado u otro. El objetivo consiste en que uno de los jugadores consiga \n"
                                       "más puntos que el oponente al finalizar el juego. Estos puntos se obtienen cuando el jugador adversario \n"
                                       "falla al devolver la pelota.",
                                  font=("Arial", 17),
                                  bg="black",
                                  fg="white",
                                  justify="left")
        descripcion_juego.place(x=20, y=90)

        descripcion_controles = Label(canvas_instrucciones,
                                      text="Controles: \n \n"
                                           "- Para los modos de un jugador, el usuario va a pode mover su barra para arriba y para abajo con\n"
                                           "Tecla W y Tecla S respectivamente y así no dejar que la bola entre a la zona que se está defendiendo,\n"
                                           "para intentar que el adversario no anote ni acumule puntos, y poder ganar.\n"
                                           "\n- Para los modos de dos jugadores, el jugador de la izquierda moverá su barra para arriba y para abajo\n"
                                           "con las teclas Tecla  W y  Tecla S respectivamente. Por otro lado, el segundo jugador usará las Flecha\n"
                                           "Arriba y Flecha Abajo respectivamente para mover arriba y abajo su barra posicionada al lado derecho\n"
                                           "de la pantalla",
                                      font=("Arial", 17),
                                      bg="black",
                                      fg="white",
                                      justify="left")
        descripcion_controles.place(x=20, y=400)

class Bola:
    def __init__(self):
        self.posicion = [11, 19]
        self.velocidad = [1, 1]
    def getPosicion(self):
        return self.posicion
    def getVelocidad(self):
        return self.velocidad
    def setPosicion(self, nuevo):
        self.posicion = nuevo
    def setVelocidad(self, nuevo):
        self.velocidad = nuevo
    def movimiento(self):
        global nivel
        global Fps
        M = juego.getMatriz()
        pos = bola.getPosicion()
        vel = bola.getVelocidad()
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 32 or M[pos[0] + vel[0]][pos[1] + vel[1]] == 31:
            vel = [-vel[0], vel[1]]
            bola.setVelocidad(vel)
            juego.setMatriz(M)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 11:
            pygame.mixer.music.load("Blip.wav")
            pygame.mixer.music.play()
            vel = [-1, -vel[1]]
            bola.setVelocidad(vel)
            juego.setMatriz(M)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 12:
            pygame.mixer.music.load("Blip.wav")
            pygame.mixer.music.play()
            vel = [0, -vel[1]]
            bola.setVelocidad(vel)
            juego.setMatriz(M)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 13:
            pygame.mixer.music.load("Blip.wav")
            pygame.mixer.music.play()
            vel = [1, -vel[1]]
            bola.setVelocidad(vel)
            juego.setMatriz(M)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 41:
            if barra2.getPuntos() > 9:
                nivel += 1
                pygame.mixer.music.load("Nivel.wav")
                pygame.mixer.music.play()
                if nivel == 2:
                    Fps = 30
                if nivel == 3:
                    Fps = 35
                barra2.setPuntos(0)
                barra1.setPuntos(0)
                juego.hacer_matriz()
                pos = [11, 19]
                bola.setPosicion(pos)
                ganador = barra2.getNiveles()
                ganador += 1
                barra2.setNiveles(ganador)
                time.sleep(0.5)
            else:
                pygame.mixer.music.load("Anota.wav")
                pygame.mixer.music.play()
                punto = barra2.getPuntos()
                punto += 1
                barra2.setPuntos(punto)
                bola.setVelocidad([1,1])
                pos = [11, 19]
                bola.setPosicion(pos)
                juego.hacer_matriz()
                time.sleep(0.1)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 42:
            if barra1.getPuntos() > 9:
                nivel += 1
                pygame.mixer.music.load("Nivel.wav")
                pygame.mixer.music.play()
                if nivel == 2:
                    Fps = 30
                if nivel == 3:
                    Fps = 35
                barra1.setPuntos(0)
                barra2.setPuntos(0)
                juego.hacer_matriz()
                pos = [11, 19]
                bola.setPosicion(pos)
                ganador = barra1.getNiveles()
                ganador += 1
                barra1.setNiveles(ganador)
                time.sleep(0.5)
            else:
                pygame.mixer.music.load("Anota.wav")
                pygame.mixer.music.play()
                punto = barra1.getPuntos()
                punto += 1
                barra1.setPuntos(punto)
                bola.setVelocidad([1, 1])
                pos = [11, 19]
                bola.setPosicion(pos)
                juego.hacer_matriz()
                time.sleep(0.1)
        else:
            M[pos[0]][pos[1]] = 0
            M[pos[0] + vel[0]][pos[1] + vel[1]] = 2
            pos = [pos[0] + vel[0], pos[1] + vel[1]]
            bola.setPosicion(pos)
            bola.setVelocidad(vel)
            juego.setMatriz(M)

class Barras:
    def __init__(self, CPU, puntos, niveles):
        self.CPU = CPU
        self.puntos = puntos
        self.niveles = niveles
    def getPuntos(self):
        return self.puntos
    def getNiveles(self):
        return self.niveles
    def getCPU(self):
        return self.CPU
    def setPuntos(self, nuevo):
        self.puntos = nuevo
    def setNiveles(self, nuevo):
        self.niveles = nuevo
    def setCPU(self, nuevo):
        self.cpu = nuevo
    def moverse(self, direccion):
        M = juego.getMatriz()
        i = 0
        if barras == 1:
            if nivel == 1:
                if direccion == "Arriba1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i - 1][2] = 11
                            M[i + 1][2] = 11
                            M[i + 2][2] = 12
                            M[i + 5][2] = 13
                            M[i + 8][2] = 0
                            M[24][2] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i][2] = 0
                            M[i + 3][2] = 11
                            M[i + 6][2] = 12
                            M[i + 9][2] = 13
                            M[0][2] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Arriba2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i - 1][37] = 11
                            M[i + 1][37] = 11
                            M[i + 2][37] = 12
                            M[i + 5][37] = 13
                            M[i + 8][37] = 0
                            M[24][37] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i][37] = 0
                            M[i + 3][37] = 11
                            M[i + 6][37] = 12
                            M[i + 9][37] = 13
                            M[0][37] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
            elif nivel == 2:
                if direccion == "Arriba1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i - 1][2] = 11
                            M[i + 1][2] = 12
                            M[i + 3][2] = 13
                            M[i + 5][2] = 0
                            M[24][2] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i][2] = 0
                            M[i + 2][2] = 11
                            M[i + 4][2] = 12
                            M[i + 6][2] = 13
                            M[0][2] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Arriba2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i - 1][37] = 11
                            M[i + 1][37] = 12
                            M[i + 3][37] = 13
                            M[i + 5][37] = 0
                            M[24][37] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i][37] = 0
                            M[i + 2][37] = 11
                            M[i + 4][37] = 12
                            M[i + 6][37] = 13
                            M[0][37] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
            else:
                if direccion == "Arriba1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i - 1][2] = 11
                            M[i][2] = 12
                            M[i + 1][2] = 13
                            M[i + 2][2] = 0
                            M[24][2] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i][2] = 0
                            M[i + 1][2] = 11
                            M[i + 2][2] = 12
                            M[i + 3][2] = 13
                            M[0][2] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Arriba2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i - 1][37] = 11
                            M[i][37] = 12
                            M[i + 1][37] = 13
                            M[i + 2][37] = 0
                            M[24][37] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i][37] = 0
                            M[i + 1][37] = 11
                            M[i + 2][37] = 12
                            M[i + 3][37] = 13
                            M[0][37] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
        else:
            if nivel == 1:
                if direccion == "Arriba1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i - 1][2] = 11
                            M[i + 1][2] = 11
                            M[i + 2][2] = 12
                            M[i + 5][2] = 13
                            M[i + 8][2] = 0
                            M[24][2] = 32
                            M[i - 1][6] = 11
                            M[i + 1][6] = 11
                            M[i + 2][6] = 12
                            M[i + 5][6] = 13
                            M[i + 8][6] = 0
                            M[24][6] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i][2] = 0
                            M[i + 3][2] = 11
                            M[i + 6][2] = 12
                            M[i + 9][2] = 13
                            M[0][2] = 31
                            M[i][6] = 0
                            M[i + 3][6] = 11
                            M[i + 6][6] = 12
                            M[i + 9][6] = 13
                            M[0][6] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Arriba2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i - 1][37] = 11
                            M[i + 1][37] = 11
                            M[i + 2][37] = 12
                            M[i + 5][37] = 13
                            M[i + 8][37] = 0
                            M[24][37] = 32
                            M[i - 1][33] = 11
                            M[i + 1][33] = 11
                            M[i + 2][33] = 12
                            M[i + 5][33] = 13
                            M[i + 8][33] = 0
                            M[24][33] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i][37] = 0
                            M[i + 3][37] = 11
                            M[i + 6][37] = 12
                            M[i + 9][37] = 13
                            M[0][37] = 31
                            M[i][33] = 0
                            M[i + 3][33] = 11
                            M[i + 6][33] = 12
                            M[i + 9][33] = 13
                            M[0][33] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
            elif nivel == 2:
                if direccion == "Arriba1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i - 1][2] = 11
                            M[i + 1][2] = 12
                            M[i + 3][2] = 13
                            M[i + 5][2] = 0
                            M[24][2] = 32
                            M[i - 1][6] = 11
                            M[i + 1][6] = 12
                            M[i + 3][6] = 13
                            M[i + 5][6] = 0
                            M[24][6] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i][2] = 0
                            M[i + 2][2] = 11
                            M[i + 4][2] = 12
                            M[i + 6][2] = 13
                            M[0][2] = 31
                            M[i][6] = 0
                            M[i + 2][6] = 11
                            M[i + 4][6] = 12
                            M[i + 6][6] = 13
                            M[0][6] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Arriba2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i - 1][37] = 11
                            M[i + 1][37] = 12
                            M[i + 3][37] = 13
                            M[i + 5][37] = 0
                            M[24][37] = 32
                            M[i - 1][33] = 11
                            M[i + 1][33] = 12
                            M[i + 3][33] = 13
                            M[i + 5][33] = 0
                            M[24][33] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i][37] = 0
                            M[i + 2][37] = 11
                            M[i + 4][37] = 12
                            M[i + 6][37] = 13
                            M[0][37] = 31
                            M[i][33] = 0
                            M[i + 2][33] = 11
                            M[i + 4][33] = 12
                            M[i + 6][33] = 13
                            M[0][33] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
            else:
                if direccion == "Arriba1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i - 1][2] = 11
                            M[i][2] = 12
                            M[i + 1][2] = 13
                            M[i + 2][2] = 0
                            M[24][2] = 32
                            M[i - 1][6] = 11
                            M[i][6] = 12
                            M[i + 1][6] = 13
                            M[i + 2][6] = 0
                            M[24][6] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo1":
                    while i != len(M[0]):
                        if M[i][2] == 11:
                            M[i][2] = 0
                            M[i + 1][2] = 11
                            M[i + 2][2] = 12
                            M[i + 3][2] = 13
                            M[0][2] = 31
                            M[i][6] = 0
                            M[i + 1][6] = 11
                            M[i + 2][6] = 12
                            M[i + 3][6] = 13
                            M[0][6] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Arriba2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i - 1][37] = 11
                            M[i][37] = 12
                            M[i + 1][37] = 13
                            M[i + 2][37] = 0
                            M[24][37] = 32
                            M[i - 1][33] = 11
                            M[i][33] = 12
                            M[i + 1][33] = 13
                            M[i + 2][33] = 0
                            M[24][33] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1
                elif direccion == "Abajo2":
                    while i != len(M[0]):
                        if M[i][37] == 11:
                            M[i][37] = 0
                            M[i + 1][37] = 11
                            M[i + 2][37] = 12
                            M[i + 3][37] = 13
                            M[0][37] = 31
                            M[i][33] = 0
                            M[i + 1][33] = 11
                            M[i + 2][33] = 12
                            M[i + 3][33] = 13
                            M[0][33] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1

barra1 = Barras(0, 0, 0)
barra2 = Barras(0, 0, 0)
bola = Bola()
juego = Juego([])
juego.hacer_matriz()
juego.menu_principal()

while not cerrar:
    if comprobar == 0:
        pantalla = pygame.display.set_mode((largo_pantalla, ancho_pantalla))
        pygame.display.set_caption("PONG")
        pantalla.fill(negro)
        comprobar = 1
    reloj.tick(Fps)
    bola.movimiento()
    control_movimiento = pygame.time.get_ticks() // 10
    tecla = pygame.key.get_pressed()
    if barra2.getCPU()==1:
        vel = bola.getVelocidad()
        if nivel == 1:
            while i != len(M[0]):
                if M[i][37] == 11:
                    if vel[0] == 1:
                        M[i][37] = 0
                        M[i + 3][37] = 11
                        M[i + 6][37] = 12
                        M[i + 9][37] = 13
                        M[0][37] = 31
                        juego.setMatriz(M)
                        break
                    elif vel[0] == -1:
                        M[i - 1][37] = 11
                        M[i + 1][37] = 11
                        M[i + 2][37] = 12
                        M[i + 5][37] = 13
                        M[i + 8][37] = 0
                        M[24][37] = 32
                        juego.setMatriz(M)
                        break
                    else:
                        break
                else:
                    i += 1
    if tecla[pygame.K_w] and juego.getMatriz()[0][2] == 31:
        barra1.moverse("Arriba1")
    if tecla[pygame.K_s] and juego.getMatriz()[24][2] == 32:
        barra1.moverse("Abajo1")
    if tecla[pygame.K_UP] and juego.getMatriz()[0][37] == 31:
        barra1.moverse("Arriba2")
    if tecla[pygame.K_DOWN] and juego.getMatriz()[24][37] == 32:
        barra1.moverse("Abajo2")
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    if barra2.getCPU() == 1:
        vel = bola.getVelocidad()
        pos = bola.getPosicion()
        i = 0
        M = juego.getMatriz()
        if pos[0] >= 6 and pos[0] <= 18:
            if nivel == 1:
                while i != len(M[0]):
                    if M[i][37] == 11:
                        if vel[0] == 1:
                            M[24][37] = 32
                            M[i][37] = 0
                            M[i + 3][37] = 11
                            M[i + 6][37] = 12
                            M[i + 9][37] = 13
                            M[0][37] = 31
                            juego.setMatriz(M)
                            break
                        elif vel[0] == -1:
                            M[0][37] = 31
                            M[i - 1][37] = 11
                            M[i + 1][37] = 11
                            M[i + 2][37] = 12
                            M[i + 5][37] = 13
                            M[i + 8][37] = 0
                            M[24][37] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            break
                    else:
                        i += 1
            elif nivel == 2:
                while i != len(M[0]):
                    if M[i][37] == 11:
                        if vel[0] == 1:
                            M[i][37] = 0
                            M[i + 2][37] = 11
                            M[i + 4][37] = 12
                            M[i + 6][37] = 13
                            M[0][37] = 31
                            juego.setMatriz(M)
                            break
                        elif vel[0] == -1:
                            M[i - 1][37] = 11
                            M[i + 1][37] = 12
                            M[i + 3][37] = 13
                            M[i + 5][37] = 0
                            M[24][37] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            break
                    else:
                        i += 1
            else:
                while i != len(M[0]):
                    if M[i][37] == 11:
                        if vel[0] == 1:
                            M[i][37] = 0
                            M[i + 1][37] = 11
                            M[i + 2][37] = 12
                            M[i + 3][37] = 13
                            M[0][37] = 31
                            juego.setMatriz(M)
                            break
                        elif vel[0] == -1:
                            M[i - 1][37] = 11
                            M[i][37] = 12
                            M[i + 1][37] = 13
                            M[i + 2][37] = 0
                            M[24][37] = 32
                            juego.setMatriz(M)
                            break
                        else:
                            break
                    else:
                        i += 1

    x = 0
    y = 0
    n = 0
    m = 0
    while n != filas:
        while m != columnas:
            if juego.getMatriz()[n][m] == 11 or juego.getMatriz()[n][m] == 12 or juego.getMatriz()[n][m] == 13 or juego.getMatriz()[n][m] == 2:
                color = blanco
            elif ((n >= 2 and n <= 3) or (n >= 6 and n <= 7) or (n >= 10 and n <= 11) or (n >= 14 and n <= 15) or (n >= 18 and n <= 19) or (n >= 22 and n <= 23)) and m == 19:
                color = blanco
            elif (barra1.getPuntos() >= 1 and n == 1 and m == 17) or (barra2.getPuntos() >= 1 and n == 1 and m == 21):
                color = blanco
            elif (barra1.getPuntos() >= 2 and n == 1 and m == 15) or (barra2.getPuntos() >= 2 and n == 1 and m == 23):
                color = blanco
            elif (barra1.getPuntos() >= 3 and n == 1 and m == 13) or (barra2.getPuntos() >= 3 and n == 1 and m == 25):
                color = blanco
            elif (barra1.getPuntos() >= 4 and n == 1 and m == 11) or (barra2.getPuntos() >= 4 and n == 1 and m == 27):
                color = blanco
            elif (barra1.getPuntos() >= 5 and n == 1 and m == 9) or (barra2.getPuntos() >= 5 and n == 1 and m == 29):
                color = blanco
            elif (barra1.getPuntos() >= 6 and n == 3 and m == 17) or (barra2.getPuntos() >= 6 and n == 3 and m == 21):
                color = blanco
            elif (barra1.getPuntos() >= 7 and n == 3 and m == 15) or (barra2.getPuntos() >= 7 and n == 3 and m == 23):
                color = blanco
            elif (barra1.getPuntos() >= 8 and n == 3 and m == 13) or (barra2.getPuntos() >= 8 and n == 3 and m == 25):
                color = blanco
            elif (barra1.getPuntos() >= 9 and n == 3 and m == 11) or (barra2.getPuntos() >= 9 and n == 3 and m == 27):
                color = blanco
            elif (barra1.getPuntos() >= 10 and n == 3 and m == 9) or (barra2.getPuntos() >= 10 and n == 3 and m == 29):
                color = blanco
            else:
                color = negro
            pygame.draw.rect(pantalla, color, [x, y, largo_cuadro, ancho_cuadro])
            x += largo_cuadro
            m += 1
        x = 0
        y += ancho_cuadro
        n += 1
        m = 0
    pygame.display.update()
    if barra1.getNiveles() == 2 or barra2.getNiveles() == 2:
        pygame.quit()