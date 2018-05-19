import pygame as pygame
import time
from tkinter import *
import random
import winsound
from threading import Thread

#Globales utilizadas por el programa

#Variable principal del while de pygame
cerrar = True

#Cantidad de filas de la matriz
filas = 25
#Cantidad de columnas de la matriz
columnas = 40

#Indice el largo de la ventana de juego
largo_pantalla = 1080
#Indica el ancho de la ventana de juego
ancho_pantalla = 720

#Variables para calcular el tamaño de los pixeles de cada cuadro de la matriz
largo_cuadro = largo_pantalla // columnas
ancho_cuadro = ancho_pantalla // filas

#Colores en RGB para usar en pygame
negro = (0, 0, 0)
blanco = (255, 255, 255)

#Varables que controlan el nivel del juego y la cantidad de barras a utilizar por jugador
nivel = 1
barras = 1

#Variables para manejar los FPS del juego
reloj = pygame.time.Clock()
Fps = 20

#Variable para abrir la ventana de pygame
comprobar = 0

#Iniciación de pygame
pygame.init()

class Juego:
    def __init__(self, M):
        #Se crea la matriz en el inicio de la clase, la matriz tiene solamente ceros
        self.M = M
        for n in range(filas):
            self.M.append([])
            for m in range(columnas):
                self.M[n].append(0)
    #Método de la clase para asignar las posiciones de los objetos en la matriz, varia dependiendo de los modos de juego elegidos
    #Los datos de la matriz varían entre 0 (nada), los que inician con 1 son las barras, 11 (posición en donde rebota la bola hacia arriba), 12 (posicion en donde rebota la bola en línea recta), 13 (posicion en donde la bola rebota hacia abajo)
    #31 (limite superior de la matriz, sirve para detener las barras y que la bola rebote), 32 (limite inferior de la matriz), 2 (la bola)
    #41 (porteria del jugador 1), 42(porteria del jugador 2)
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
                        elif n >= 7 and n <= 9 and m == 8:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 8:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 8:
                            self.M[n][m] = 13
                        elif n >= 7 and n <= 15 and m == 37:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 37:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 37:
                            self.M[n][m] = 13
                        elif n >= 7 and n <= 15 and m == 31:
                            self.M[n][m] = 11
                        elif n >= 10 and n <= 12 and m == 31:
                            self.M[n][m] = 12
                        elif n >= 13 and n <= 15 and m == 31:
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
                        elif n >= 11 and n <= 12 and m == 8:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 8:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 8:
                            self.M[n][m] = 13
                        elif n >= 11 and n <= 12 and m == 37:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 37:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 37:
                            self.M[n][m] = 13
                        elif n >= 11 and n <= 12 and m == 31:
                            self.M[n][m] = 11
                        elif n >= 13 and n <= 14 and m == 31:
                            self.M[n][m] = 12
                        elif n >= 15 and n <= 16 and m == 31:
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
                        elif n == 11 and m == 8:
                            self.M[n][m] = 11
                        elif n == 12 and m == 8:
                            self.M[n][m] = 12
                        elif n == 13 and m == 8:
                            self.M[n][m] = 13
                        elif n == 11 and m == 37:
                            self.M[n][m] = 11
                        elif n == 12 and m == 37:
                            self.M[n][m] = 12
                        elif n == 13 and m == 37:
                            self.M[n][m] = 13
                        elif n == 11 and m == 31:
                            self.M[n][m] = 11
                        elif n == 12 and m == 31:
                            self.M[n][m] = 12
                        elif n == 13 and m == 31:
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
    #Métodos para obtener la matriz del juego y para sobreescribirla
    def getMatriz(self):
        return self.M
    def setMatriz(self, nuevo):
        self.M = nuevo
    #Método para abrir la ventana del ganador de la partida
    def ganador(self):
        #Es necesario volver a iniciar pygame porque se cerró al terminar la partida
        pygame.init()

        #Creación de la ventana en tKinter y se le coloca un canvas
        ganador = Tk()
        ganador.title("Ganador")
        ganador.minsize(550, 300)
        ganador.maxsize(550, 300)

        canvasg = Canvas(ganador, width=1080, height=720, bg="black")
        canvasg.place(x=-2, y=-2)
        canvasg.pack()

        #Función que permite volver al menú principal del juego
        def ganador_aux():
            ganador.destroy()
            juego.menu_principal()

        #Función que se activa con un thread para reproducir el sonido de ganador
        def sonido_ganador():
            winsound.PlaySound("Ganador.wav", winsound.SND_ALIAS)

        #Botones y labels de la ventana
        bt_listo = Button(canvasg,
                          text="Listo",
                          font=("Arial", 16),
                          width=14,
                          bg="white",
                          command=ganador_aux)
        bt_listo.place(x=180, y=200)

        if barra1.getNiveles() == 2:
            gano = Label(canvasg,
                         text="Felicidades Jugador 1",
                         font=("Arial", 20),
                         bg="black",
                         fg="white")
            gano.place(x=145, y=30)
        if barra2.getNiveles() == 2:
            gano = Label(canvasg,
                         text="Felicidades Jugador 2",
                         font=("Arial", 20),
                         bg="black",
                         fg="white")
            gano.place(x=145, y=30)

        #Thread para iniciar el sonido
        t1 = Thread(target = sonido_ganador, args=())
        t1.start()

        ganador.mainloop()
    #Método para abrir la ventana del menú principal
    def menu_principal(self):
        #Se reinician las globales a sus valores originales y atributos
        global barras
        global Fps
        global comprobar
        global cerrar
        global nivel
        barras = 1
        nivel = 1
        cerrar = True
        comprobar = 0
        Fps = 20
        juego.hacer_matriz()
        bola.setVelocidad([1, 1])
        bola.setPosicion([11,19])
        barra1.setPuntos(0)
        barra2.setPuntos(0)
        barra1.setNiveles(0)
        barra2.setNiveles(0)

        #Creación de la ventana del menú principal y se loe coloca un canvas
        ventana = Tk()
        ventana.title("Menu Principal")
        ventana.minsize(1080, 720)
        ventana.resizable(width=NO, height=NO)

        canvas = Canvas(ventana, width=1080, height=720, bg="black")
        canvas.place(x=-2, y=-2)
        canvas.pack()

        #Funciónes para llamar a los modos de juego o otras ventanas, y cerrar la del menú principal
        def jugador_CPU_aux():
            ventana.destroy()
            juego.jugador_CPU()

        def jugador_singles_aux():
            ventana.destroy()
            juego.jugador_singles()

        def jugador_doubles_aux():
            ventana.destroy()
            juego.jugador_doubles()

        def ventana_modos_aux():
            ventana.withdraw()
            juego.ventana_modos()

        def ventana_instrucciones_aux():
            ventana.withdraw()
            juego.ventana_instrucciones()

        #Botones para jugar
        un_jugador = Button(canvas,
                            text="Un jugador",
                            font=("Arial", 20),
                            width=14,
                            bg="white",
                            command=jugador_CPU_aux)
        un_jugador.place(x=425, y=250)

        bt_singles = Button(canvas,
                            text="Singles",
                            font=("Arial", 20),
                            width=14,
                            bg="white",
                            command=jugador_singles_aux)
        bt_singles.place(x=425, y=380)

        bt_doubles = Button(canvas,
                            text="Doubles",
                            font=("Arial", 20),
                            width=14,
                            bg="white",
                            command=jugador_doubles_aux)
        bt_doubles.place(x=425, y=450)

        #Botón para acceder a la pantalla de los modos de juego
        bt_modos = Button(canvas,
                               text="Modos",
                               font=("Arial", 20),
                               width=14,
                               bg="white",
                               command=ventana_modos_aux)
        bt_modos.place(x=425, y=580)

        #Botón para acceder a la instrucciones
        bt_instrucciones = Button(canvas,
                                  text="Instrucciones",
                                  font=("Arial", 20),
                                  width=14,
                                  bg="white",
                                  command=ventana_instrucciones_aux)
        bt_instrucciones.place(x=425, y=650)

        #Labels de la ventana
        titulo = Label(canvas,
                       text="PONG",
                       font=("Arial", 78),
                       bg="black",
                       fg="white")
        titulo.place(x=390, y=15)

        # Fin del loop
        ventana.mainloop()

    #Funciones para iniciar los modos de juego
    def jugador_CPU(self):
        global cerrar
        barra2.setCPU(1)
        cerrar = False
    def jugador_singles(self):
        global cerrar
        barra2.setCPU(0)
        cerrar = False
    def jugador_doubles(self):
        global cerrar
        global barras
        barras = 2
        barra2.setCPU(0)
        juego.hacer_matriz()
        cerrar = False

    #Método para abrir la ventana que explica los modos de juego
    def ventana_modos(self):
        #Creación de la ventana y su colocación del canvas
        ventana_modos = Tk()
        ventana_modos.title("Modos de Juego")
        ventana_modos.minsize(1080, 720)
        ventana_modos.resizable(width=NO, height=NO)

        canvas_modos = Canvas(ventana_modos, width=1080, height=720, bg="black")
        canvas_modos.place(x=-2, y=-2)
        canvas_modos.pack()

        #Función para volver al menú principal
        def volver():
            ventana_modos.destroy()
            juego.menu_principal()

        #Botón para volver al menú principal
        atras = Button(canvas_modos,
                       text="Volver al Menú Principal",
                       font=("Arial", 16),
                       bg="white",
                       command=volver)
        atras.place(x=820, y=25)

        #Labels con descripciones de modos de juego
        descripcion_singles = Label(canvas_modos,
                                    text="Modo Singles es un un tipo de juego en el que participan\n dos jugadores, y cada jugador controla una paleta",
                                    font=("Arial", 20),
                                    bg="black",
                                    fg="white")
        descripcion_singles.place(x=200, y=200)

        descripcion_doubles = Label(canvas_modos,
                                    text="Modo Doubles: a diferencia del Modo Singles, este es un un tipo de juego\n en el que participan dos jugadores, y cada jugador controla dos paletas",
                                    font=("Arial", 20),
                                    bg="black",
                                    fg="white")
        descripcion_doubles.place(x=95, y=500)

        lb_doubles = Label(canvas_modos,
                                    text="Modo Doubles",
                                    font=("Arial", 30),
                                    bg="white",
                                    fg="black")
        lb_doubles.place(x=400, y=425)

        lb_singles = Label(canvas_modos,
                                    text="Modo Singles",
                                    font=("Arial", 30),
                                    bg="white",
                                    fg="black")
        lb_singles.place(x=410, y=125)

    #Método para abrir la ventana de las instrucciones del juego
    def ventana_instrucciones(self):
        #Creación de la ventana y su canvas
        ventana_instrucciones = Tk()
        ventana_instrucciones.title("Intrucciones")
        ventana_instrucciones.minsize(1080, 720)
        ventana_instrucciones.resizable(width=NO, height=NO)

        canvas_instrucciones = Canvas(ventana_instrucciones, width=1080, height=720, bg="black")
        canvas_instrucciones.place(x=-2, y=-2)
        canvas_instrucciones.pack()

        #Función para volver al menú principal
        def volver():
            ventana_instrucciones.destroy()
            juego.menu_principal()

        #Botón para volver al menú principal
        atras = Button(canvas_instrucciones,
                       text="Volver al Menú Principal",
                       font=("Arial", 16),
                       bg="white",
                       command=volver)
        atras.place(x=820, y=25)

        #Labels de descripcion del juego y sus controles
        descripcion_juego = Label(canvas_instrucciones,
                                  text="Descripción: \n \n"
                                       "Pong es un juego de deportes en dos dimensiones que simula un tenis de mesa. \n"
                                       "El jugador controla en el juego una paleta moviéndola verticalmente en la parte izquierda de la pantalla,\n"
                                       "y puede competir tanto contra un oponente controlado por computadora, como con otro jugador\n"
                                       "humano que controla una segunda paleta en la parte opuesta. Los jugadores pueden usar las paletas\n"
                                       "para pegarle a la pelota hacia un lado u otro. El objetivo consiste en que uno de los jugadores consiga \n"
                                       "11 puntos para pasar al siguiente nivel. Estos puntos se obtienen cuando el jugador adversario \n"
                                       "falla al devolver la pelota. Para ganar un jugador debe ganar dos de los tres niveles.",
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
    #Atributos de la bola
    def __init__(self, velocidad, posicion):
        self.posicion = posicion
        self.velocidad = velocidad
    #Métodos para obtener y sobreescribir la velocidad y posicion de la bola en la matriz
    def getPosicion(self):
        return self.posicion
    def getVelocidad(self):
        return self.velocidad
    def setPosicion(self, nuevo):
        self.posicion = nuevo
    def setVelocidad(self, nuevo):
        self.velocidad = nuevo
    #Método para el movimiento de la bola en la matriz, la velocidad de ella conforme avanzan niveles depende de los FPS del juego
    #La bola para moverse utilizará su posición actual, y la sumará la velocidad en fila y columna para obtener el espacio al que se moverá
    #En caso de que el espacio siguiente sea 0, avanzará
    #En caso de que sea, 11, 12, 13, 31 o 32, la bola rebotará hacia cierta dirección
    #En caso de que sea un 41 o un 42, se sumará un punto a la barra correspondiente
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
                if ganador != 2:
                    pygame.mixer.music.load("Nivel.wav")
                    pygame.mixer.music.play()
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
                if ganador != 2:
                    pygame.mixer.music.load("Nivel.wav")
                    pygame.mixer.music.play()
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
    #Atributos de la barras
    def __init__(self, CPU, puntos, niveles):
        self.CPU = CPU
        self.puntos = puntos
        self.niveles = niveles
    #Métodos para obtener y sobreescribir los puntos, niveles ganados y el boolean para saber si es CPU de las barras
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
        self.CPU = nuevo
    #Método para reaizar los movimientos manuales (no cpu) de las barras
    #Para moverse, se recibirá la tecla presionada por el usuario, (w arriba del jugador 1, s abajo del jugador 1, flecha arriba del jugador 2 y flecha abajo del jugador 2)
    #Lo que hace es que empieza a leer la columna hasta encontrar el primer elemento de la barra en ella, a partir de ahí empezará a escirbir datos en la matriz con base al índice
    #Varía dependiendo de las barras utilizadas y el nivel
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
                            M[i - 1][8] = 11
                            M[i + 1][8] = 11
                            M[i + 2][8] = 12
                            M[i + 5][8] = 13
                            M[i + 8][8] = 0
                            M[24][8] = 32
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
                            M[i][8] = 0
                            M[i + 3][8] = 11
                            M[i + 6][8] = 12
                            M[i + 9][8] = 13
                            M[0][8] = 31
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
                            M[i - 1][31] = 11
                            M[i + 1][31] = 11
                            M[i + 2][31] = 12
                            M[i + 5][31] = 13
                            M[i + 8][31] = 0
                            M[24][31] = 32
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
                            M[i][31] = 0
                            M[i + 3][31] = 11
                            M[i + 6][31] = 12
                            M[i + 9][31] = 13
                            M[0][31] = 31
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
                            M[i - 1][8] = 11
                            M[i + 1][8] = 12
                            M[i + 3][8] = 13
                            M[i + 5][8] = 0
                            M[24][8] = 32
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
                            M[i][8] = 0
                            M[i + 2][8] = 11
                            M[i + 4][8] = 12
                            M[i + 6][8] = 13
                            M[0][8] = 31
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
                            M[i - 1][31] = 11
                            M[i + 1][31] = 12
                            M[i + 3][31] = 13
                            M[i + 5][31] = 0
                            M[24][31] = 32
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
                            M[i][31] = 0
                            M[i + 2][31] = 11
                            M[i + 4][31] = 12
                            M[i + 6][31] = 13
                            M[0][31] = 31
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
                            M[i - 1][8] = 11
                            M[i][8] = 12
                            M[i + 1][8] = 13
                            M[i + 2][8] = 0
                            M[24][8] = 32
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
                            M[i][8] = 0
                            M[i + 1][8] = 11
                            M[i + 2][8] = 12
                            M[i + 3][8] = 13
                            M[0][8] = 31
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
                            M[i - 1][31] = 11
                            M[i][31] = 12
                            M[i + 1][31] = 13
                            M[i + 2][31] = 0
                            M[24][31] = 32
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
                            M[i][31] = 0
                            M[i + 1][31] = 11
                            M[i + 2][31] = 12
                            M[i + 3][31] = 13
                            M[0][31] = 31
                            juego.setMatriz(M)
                            break
                        else:
                            i += 1

#Se crean las instancias de las barras del jugador 1 y 2, el primer argumento es un boolean para indicar si es un cpu o no, el segundo son los puntos de la barra y el tercero son los niveles ganados
barra1 = Barras(0, 0, 0)
barra2 = Barras(0, 0, 0)

#Se crea la instancia de la bola, el primer argumento será la velocidad de la fila y columna de la bola y el segundo será su posición inicial en la matriz
bola = Bola([1,1],[11,19])

#Se crea la instancia del juego, su argumento es la matriz a crear
juego = Juego([])
#Se abre el menú principal
juego.menu_principal()

#Función para obtener un valor entre 0 y 1, con tal de limitar el movimiento del cpu y que no sea imposible ganarle en el primer nivel
#E: Función
#S: Un número entre 0 y 1
#R: Solo debe ser uno de esos dos números
def hacer_random():
    if nivel == 1:
        ran = random.randint(0, 1)
        return ran
    else:
        return 0

#While principal de pygame
while not cerrar:
    #Caso que solo se ejectua una vez por partida para abrir la ventana del juego
    if comprobar == 0:
        pantalla = pygame.display.set_mode((largo_pantalla, ancho_pantalla))
        pygame.display.set_caption("PONG")
        pantalla.fill(negro)
        comprobar = 1

    #Método de pygame para controlar la velocidad del juego con los Fps
    reloj.tick(Fps)
    #Se invoca el método de movimiento de la bola
    bola.movimiento()
    #Variable que obtiene la tecla presionada por el usuario
    tecla = pygame.key.get_pressed()
    #Variable que obtiene un valor al azar entre 0 y 1
    ran = hacer_random()

    #Casos para detectar la tecla presionada y mover alguna de las barras o cerrar el juego
    if tecla[pygame.K_w] and juego.getMatriz()[0][2] == 31:
        barra1.moverse("Arriba1")
    if tecla[pygame.K_s] and juego.getMatriz()[24][2] == 32:
        barra1.moverse("Abajo1")
    if tecla[pygame.K_UP] and juego.getMatriz()[0][37] == 31 and barra2.getCPU() == 0:
        barra1.moverse("Arriba2")
    if tecla[pygame.K_DOWN] and juego.getMatriz()[24][37] == 32 and barra2.getCPU() == 0:
        barra1.moverse("Abajo2")
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    #Caso del movimiento de la barra 2, en caso de que sea un cpu
    #Funciona de manera similar al método de movimiento de la barras manual, con la diferencia de que esta seguirá a la posicion de la fila de la bola
    #Para que no sea imposible, se le pone una restricción en el nivel 1 que solo tiene permitido moverse cuando el número azar conseguido sea 0 y la bola se encuentre en cierto rango, para que no tenga problemas con la matriz
    if barra2.getCPU() == 1:
        vel = bola.getVelocidad()
        pos = bola.getPosicion()
        i = 0
        M = juego.getMatriz()
        if pos[0] >= 5 and pos[0] <= 16 and ran == 0:
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

    #While que se encarga de dibujar la matriz en la pantalla, por cada vez que se presente un cambio en a matriz, esta función la reflejará de inmediato en la pantalla de juego
    #La función lee columna por columna y luego pasa a la siguiente fila, si encuentra una barra o la bola, dibuja un cuadro blanco
    #Si se encuentra en la columna central y en ciertas fila, dibujará la línea central
    #Si alguna de las dos barras anota, dibujará un cuadro blanco en la parte superior de la pantalla
    #Sino dibujará un cuadro negro
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

    #Caso en caso de que el juego termine
    if barra1.getNiveles() == 2 or barra2.getNiveles() == 2:
        cerrar = True
        pygame.quit()
        juego.ganador()
