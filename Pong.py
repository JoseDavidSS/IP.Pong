import pygame as pygame
from time import time
from time import sleep
from tkinter import *
from tkinter import messagebox
import random
import winsound
from threading import Thread
import serial

ser = serial.Serial('COM3', 9600, timeout=0)

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
ancho_pantalla = 700

#Variables para calcular el tamaño de los pixeles de cada cuadro de la matriz
largo_cuadro = largo_pantalla // columnas
ancho_cuadro = ancho_pantalla // filas

#Colores en RGB para usar en pygame
color1 = (0, 0, 0)
color2 = (255, 255, 255)

#Varables que controlan el nivel del juego y la cantidad de barras a utilizar por jugador
nivel = 1
barras = 1

#Variables para manejar los FPS del juego
reloj = pygame.time.Clock()
Fps = 20

#Variable para abrir la ventana de pygame
comprobar = 0
nueva_puntuacion = 0

t_inicio = 0

p1 = []
p2 = []
p3 = []

trampolines = 0

practica = 0

volumen = 0

#Iniciación de pygame
pygame.init()

def leerpuntuaciones():
    global p1
    global p2
    global p3
    arch = open("Puntuaciones.txt", "r")
    a = arch.readline()
    p1 = a.split(",")[:3]
    a = arch.readline()
    p2 = a.split(",")[:3]
    a = arch.readline()
    p3 = a.split(",")[:3]
    arch.close()

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
    def agregar_trampolines(self):
        if nivel == 1:
            ran1 = random.randint(6, 10)
            ran2 = random.randint(6, 10)
            ran3 = random.randint(17, 21)
            ran4 = random.randint(17, 21)
            self.M[ran1 - 1][15] = 11
            self.M[ran1][15] = 12
            self.M[ran1 + 1][15] = 13
            self.M[ran2 - 1][23] = 11
            self.M[ran2][23] = 12
            self.M[ran2 + 1][23] = 13
            self.M[ran3 - 1][15] = 11
            self.M[ran3][15] = 12
            self.M[ran3 + 1][15] = 13
            self.M[ran4 - 1][23] = 11
            self.M[ran4][23] = 12
            self.M[ran4 + 1][23] = 13
        elif nivel == 2:
            ran3 = random.randint(6, 10)
            ran4 = random.randint(6, 10)
            ran5 = random.randint(17, 21)
            ran6 = random.randint(17, 21)
            ran7 = random.randint(17, 21)
            ran8 = random.randint(19, 21)
            self.M[5][16] = 11
            self.M[6][16] = 12
            self.M[7][16] = 13
            self.M[5][22] = 11
            self.M[6][22] = 12
            self.M[7][22] = 13
            self.M[ran5 - 1][16] = 11
            self.M[ran5][16] = 12
            self.M[ran5 + 1][16] = 13
            self.M[ran6 - 1][22] = 11
            self.M[ran6][22] = 12
            self.M[ran6 + 1][22] = 13
            self.M[ran3 - 1][12] = 11
            self.M[ran3][12] = 12
            self.M[ran3 + 1][12] = 13
            self.M[ran4 - 1][26] = 11
            self.M[ran4][26] = 12
            self.M[ran4 + 1][26] = 13
            self.M[ran7 - 1][12] = 11
            self.M[ran7][12] = 12
            self.M[ran7 + 1][12] = 13
            self.M[ran8 - 1][26] = 11
            self.M[ran8][26] = 12
            self.M[ran8 + 1][26] = 13
        else:
            ran1 = random.randint(6, 8)
            ran2 = random.randint(6, 9)
            ran4 = random.randint(6, 10)
            ran5 = random.randint(17, 21)
            ran6 = random.randint(17, 21)
            ran7 = random.randint(17, 21)
            ran8 = random.randint(20, 21)
            ran9 = random.randint(6, 20)
            ran10 = random.randint(6, 20)
            self.M[ran1 - 1][16] = 11
            self.M[ran1][16] = 12
            self.M[ran1 + 1][16] = 13
            self.M[ran2 - 1][22] = 11
            self.M[ran2][22] = 12
            self.M[ran2 + 1][22] = 13
            self.M[ran5 - 1][16] = 11
            self.M[ran5][16] = 12
            self.M[ran5 + 1][16] = 13
            self.M[ran6 - 1][22] = 11
            self.M[ran6][22] = 12
            self.M[ran6 + 1][22] = 13
            self.M[5][12] = 11
            self.M[6][12] = 12
            self.M[7][12] = 13
            self.M[ran4 - 1][26] = 11
            self.M[ran4][26] = 12
            self.M[ran4 + 1][26] = 13
            self.M[ran7 - 1][12] = 11
            self.M[ran7][12] = 12
            self.M[ran7 + 1][12] = 13
            self.M[ran8 - 1][26] = 11
            self.M[ran8][26] = 12
            self.M[ran8 + 1][26] = 13
            self.M[ran9 - 1][5] = 11
            self.M[ran9][5] = 12
            self.M[ran9 + 1][5] = 13
            self.M[ran10 - 1][34] = 11
            self.M[ran10][34] = 12
            self.M[ran10 + 1][34] = 13
    def modo_practica(self):
        for i in range(filas):
            self.M[i][39] = 33
        if nivel == 1:
            for i in range(7, 16):
                self.M[i][37] = 0
        elif nivel == 2:
            for i in range(11, 17):
                self.M[i][37] = 0
        else:
            for i in range(11, 14):
                self.M[i][37] = 0
    def getMatriz(self):
        return self.M
    def setMatriz(self, nuevo):
        self.M = nuevo
    #Método para abrir la ventana del ganador de la partida
    def cambiarColor(self):
        global color1
        global color2
        if color1 == (0, 0, 0):
            color1 = (255, 255, 255)
            color2 = (0, 0, 0)
        elif color1 == (255, 255, 255):
            color1 = (118, 54, 38)
            color2 = (51, 107, 135)
        elif color1 == (118, 54, 38):
            color1 = (80, 81, 96)
            color2 = (104, 130, 158)
        elif color1 == (80, 81, 96):
            color1 = (0, 68, 69)
            color2 = (44, 120, 115)
        else:
            color1 = (0, 0, 0)
            color2 = (255, 255, 255)
    def ganador(self):
        #Es necesario volver a iniciar pygame porque se cerró al terminar la partida
        pygame.init()

        #Creación de la ventana en tKinter y se le coloca un canvas
        ganador = Tk()
        ganador.title("Ganador")
        ganador.minsize(550, 460)
        ganador.maxsize(550, 460)

        canvasg = Canvas(ganador, width=550, height=500, bg="black")
        canvasg.place(x=-2, y=-2)
        canvasg.pack()

        ptitulo = Label(canvasg,
                        text="Mejores Tiempos:",
                        font=("Fixedsys", 20),
                        bg="black",
                        fg="white")
        ptitulo.place(x=10, y=90)

        puntua = Label(canvasg,
                       text = "1. " + p1[0] + " y " + p1[1] + " con: " + str(int(p1[2]) // 60) + ":" + str(int(p1[2]) % 60) + " min" + "\n \n" + "2. " + p2[0] + " y " + p2[1] + " con: " + str(int(p2[2]) // 60) + ":" + str(int(p2[2]) % 60) + " min" + "\n \n" + "3. " + p3[0] + " y " + p3[1] + " con: " + str(int(p3[2]) // 60) + ":" + str(int(p3[2]) % 60) + " min",
                       font = ("Fixedsys", 20),
                       bg = "black",
                       fg = "white")
        puntua.place(x = 60, y = 160)

        #Función que permite volver al menú principal del juego
        def ganador_aux():
            ganador.destroy()
            juego.menu_principal()

        #Función que se activa con un thread para reproducir el sonido de ganador
        def sonido_ganador():
            if volumen == 0:
                winsound.PlaySound("Ganador.wav", winsound.SND_ALIAS)

        #Botones y labels de la ventana
        bt_listo = Button(canvasg,
                          text="Listo",
                          font=("Fixedsys", 16),
                          width=14,
                          bg="white",
                          command=ganador_aux)
        bt_listo.place(x=200, y=400)

        if barra1.getNiveles() == 2:
            gano = Label(canvasg,
                         text="Felicidades Jugador 1",
                         font=("Fixedsys", 20),
                         bg="black",
                         fg="white")
            gano.place(x=100, y=30)
        if barra2.getNiveles() == 2:
            gano = Label(canvasg,
                         text="Felicidades Jugador 2",
                         font=("Fixedsys", 20),
                         bg="black",
                         fg="white")
            gano.place(x=100, y=30)

        #Thread para iniciar el sonido
        t1 = Thread(target = sonido_ganador, args=())
        t1.start()

        ganador.mainloop()
    def nuevaPuntuacion(self, tiempo):
        pygame.init()

        nuevapunt = Tk()
        nuevapunt.title("FELICITACIONES")
        nuevapunt.minsize(800, 500)
        nuevapunt.maxsize(800, 500)

        canvasn = Canvas(nuevapunt, width = 800, height = 500, bg = "black")
        canvasn.place(x=-2, y=-2)
        canvasn.pack()

        fel = Label(canvasn,
                    text="¡¡FELICITACIONES!!\n CONSIGUIERON UN NUEVO MEJOR TIEMPO",
                    font=("Fixedsys", 20),
                    bg="black",
                    fg="white")
        fel.place(x=100, y=10)

        datos = Label(canvasn,
                      text = "Por favor, Introducir las Iniciales de los Jugadores:",
                      font = ("Fixedsys", 15),
                      bg = "black",
                      fg = "white")
        datos.place(x = 120, y = 150)

        juga1 = Label(canvasn,
                      text = "Jugador 1",
                      font = ("Fixedsys", 15),
                      bg = "black",
                      fg = "white")
        juga1.place(x = 190, y = 200)

        juga1 = Label(canvasn,
                      text="Jugador 2",
                      font=("Fixedsys", 15),
                      bg="black",
                      fg="white")
        juga1.place(x=480, y=200)

        jug1 = Entry(canvasn, bg = "white", fg = "black", font = ("Fixedsys"))
        jug1.place(x = 150, y = 260)

        jug2 = Entry(canvasn, bg="white", fg="black", font=("Fixedsys"))
        jug2.place(x = 440, y = 260)

        def nuevapuntacion_aux():
            ini1 = jug1.get()
            ini2 = jug2.get()
            if len(ini1) == 3 and len(ini2) == 3:
                ini1 = ini1.upper()
                ini2 = ini2.upper()
                nuevapunt.destroy()
                juego.escribirTiempo(tiempo, ini1, ini2)
            else:
                messagebox.showinfo("Error", "Las iniciales no deben tener más de 3 caracteres.")
                jug1.delete(0, END)
                jug2.delete(0, END)

        bt_salir = Button(canvasn,
                          text = "Listo",
                          font=("Fixedsys", 16),
                          width=14,
                          bg="white",
                          command = nuevapuntacion_aux)
        bt_salir.place(x=300, y=400)

        def sonido_puntuacion():
            if volumen == 0:
                winsound.PlaySound("Puntuacion.wav", winsound.SND_ALIAS)

        if barra1.getNiveles() == 2:
            gano = Label(canvasn,
                         text="Felicidades Jugador 1",
                         font=("Fixedsys", 16),
                         bg="black",
                         fg="white")
            gano.place(x=270, y=330)
        if barra2.getNiveles() == 2:
            gano = Label(canvasn,
                         text="Felicidades Jugador 2",
                         font=("Fixedsys", 16),
                         bg="black",
                         fg="white")
            gano.place(x=270, y=330)
        if nueva_puntuacion == 1:
            superaron = Label(canvasn,
                              text = "¡Superaron el mejor tiempo!",
                              font = ("Fixedsys", 15),
                              bg = "black",
                              fg = "white")
            superaron.place(x = 240, y = 100)
        if nueva_puntuacion == 2:
            superaron = Label(canvasn,
                              text="¡Superaron el mejor tiempo!",
                              font=("Fixedsys", 15),
                              bg="black",
                              fg="white")
            superaron.place(x=240, y=100)
        if nueva_puntuacion == 3:
            superaron = Label(canvasn,
                              text="¡Superaron el mejor tiempo!",
                              font=("Fixedsys", 15),
                              bg="black",
                              fg="white")
            superaron.place(x=240, y=100)

        t1 = Thread(target=sonido_puntuacion, args=())
        t1.start()

        nuevapunt.mainloop()
    def escribirTiempo(self, tiempo, ini1, ini2):
        global p1
        global p2
        global p3
        if nueva_puntuacion == 1:
            p1 = [ini1, ini2, str(tiempo)]
        if nueva_puntuacion == 2:
            p2 = [ini1, ini2, str(tiempo)]
        if nueva_puntuacion == 3:
            p3 = [ini1, ini2, str(tiempo)]
        arch = open("Puntuaciones.txt", "w")
        arch.write(p1[0])
        arch.write(",")
        arch.write(p1[1])
        arch.write(",")
        arch.write(p1[2])
        arch.write(",")
        arch.write("\n")
        arch.write(p2[0])
        arch.write(",")
        arch.write(p2[1])
        arch.write(",")
        arch.write(p2[2])
        arch.write(",")
        arch.write("\n")
        arch.write(p3[0])
        arch.write(",")
        arch.write(p3[1])
        arch.write(",")
        arch.write(p3[2])
        arch.write(",")
        arch.write("\n")
        arch.close()

        juego.menu_principal()
    def pausa(self):
        global volumen
        a = False
        while not a:
            try:
                entrada = str(ser.readline())
                dato = entrada[entrada.index("'") + 1: entrada.index("\\")]
                if (dato == "p"):
                    if volumen == 0:
                        pygame.mixer.music.load("Pausa.wav")
                        pygame.mixer.music.play()
                    a = True
                if(dato == "v"):
                    if volumen == 0:
                        volumen = 1
                    else:
                        volumen = 0
            except:
                pass

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        if volumen == 0:
                            pygame.mixer.music.load("Pausa.wav")
                            pygame.mixer.music.play()
                        a = True
                    if evento.key == pygame.K_m:
                        t2 = Thread(target=juego.ventanaMatriz(), args=())
                        t2.start()
                    if evento.key == pygame.K_v:
                        if volumen == 0:
                            volumen = 1
                        else:
                            volumen = 0
    def imprimirMatriz(self, M, n, i, txt, res):
        if i == (n - 1):
            res = str(M[i])
            res = res.replace(",", " ")
            txt += res + "]"
            return txt
        elif i == 0:
            res = str(M[0])
            res = res.replace(",", " ")
            txt = "[" + res + "\n"
            return juego.imprimirMatriz(M, n, i + 1, txt, res)
        else:
            res = str(M[i])
            res = res.replace(",", " ")
            txt += res + "\n"
            return juego.imprimirMatriz(M, n, i + 1, txt, "")
    def ventanaMatriz(self):
        ventanam = Tk()
        ventanam.title("Matriz Actual")
        ventanam.minsize(1310, 500)
        ventanam.maxsize(1310, 500)

        canvasm = Canvas(ventanam, width=1310, height=500, bg="black")
        canvasm.place(x=-2, y=-2)
        canvasm.pack()

        matriz = juego.imprimirMatriz(self.M, len(self.M), 0, '', '')

        lmatriz = Label(canvasm,
                        text=matriz,
                        font=("Fixedsys", 10),
                        bg="black",
                        fg="white")
        lmatriz.place(x=10, y=10)

        t_actual = time()
        t_actual -= t_inicio
        t_actual = int(t_actual)
        min = t_actual // 60
        seg = t_actual % 60

        cont = Label(canvasm,
                     text = "Contador: " + str(min) + ":" + str(seg).zfill(2),
                     font = ("Fixedsys", 14),
                     bg = "black",
                     fg = "white")
        cont.place(x = 10, y = 450)

        bt_cerrar = Button(canvasm,
                            text="Cerrar",
                            font=("Fixedsys", 8),
                            width=10,
                            bg="white",
                            command=ventanam.destroy)
        bt_cerrar.place(x=1200, y=450)

        ventanam.mainloop()
    #Método para abrir la ventana del menú principal
    def menu_principal(self):
        #Se reinician las globales a sus valores originales y atributos
        global barras
        global Fps
        global comprobar
        global cerrar
        global nivel
        global color1
        global color2
        global nueva_puntuacion
        global trampolines
        global practica
        practica = 0
        trampolines = 0
        nueva_puntuacion = 0
        color1 = (0, 0, 0)
        color2 = (255, 255, 255)
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
            ventana.destroy()
            juego.ventana_modos()

        def ventana_instrucciones_aux():
            ventana.destroy()
            juego.ventana_instrucciones()

        def ventana_practica_aux():
            ventana.destroy()
            juego.ventana_practica()

        def activar_desactivar_t():
            global trampolines
            if trampolines == 1:
                act_des.config(text = "Desactivado")
                trampolines = 0
            else:
                act_des.config(text="Activado")
                trampolines = 1

        bt_trampolines = Button(canvas,
                                text ="Trampolines",
                                font=("Fixedsys", 10),
                                bg="white",
                                command=activar_desactivar_t)
        bt_trampolines.place(x=440, y=170)

        bt_practica = Button(canvas,
                             text="Práctica",
                             font=("Fixedsys", 20),
                             width=14,
                             bg="white",
                             command=ventana_practica_aux)
        bt_practica.place(x=425, y=290)

        #Botones para jugar
        un_jugador = Button(canvas,
                            text="Un jugador",
                            font=("Fixedsys", 20),
                            width=14,
                            bg="white",
                            command=jugador_CPU_aux)
        un_jugador.place(x=425, y=220)

        bt_singles = Button(canvas,
                            text="Singles",
                            font=("Fixedsys", 20),
                            width=14,
                            bg="white",
                            command=jugador_singles_aux)
        bt_singles.place(x=425, y=380)

        bt_doubles = Button(canvas,
                            text="Doubles",
                            font=("Fixedsys", 20),
                            width=14,
                            bg="white",
                            command=jugador_doubles_aux)
        bt_doubles.place(x=425, y=450)

        #Botón para acceder a la pantalla de los modos de juego
        bt_modos = Button(canvas,
                               text="Modos",
                               font=("Fixedsys", 20),
                               width=14,
                               bg="white",
                               command=ventana_modos_aux)
        bt_modos.place(x=425, y=580)

        #Botón para acceder a la instrucciones
        bt_instrucciones = Button(canvas,
                                  text="Instrucciones",
                                  font=("Fixedsys", 20),
                                  width=14,
                                  bg="white",
                                  command=ventana_instrucciones_aux)
        bt_instrucciones.place(x=425, y=650)

        #Labels de la ventana
        act_des = Label(canvas,
                        text="Desactivado",
                        font=("Fixedsys", 10),
                        bg="black",
                        fg="white")
        act_des.place(x=543, y=172)

        titulo = Label(canvas,
                       text="PONG",
                       font=("Fixedsys", 78),
                       bg="black",
                       fg="white")
        titulo.place(x=440, y=30)

        # Fin del loop
        ventana.mainloop()
    #Funciones para iniciar los modos de juego
    def jugador_CPU(self):
        ser.write(b"0")
        global t_inicio
        global cerrar
        if trampolines == 1:
            juego.agregar_trampolines()
        t_inicio = time()
        barra2.setCPU(1)
        cerrar = False
    def jugador_singles(self):
        ser.write(b"0")
        global t_inicio
        global cerrar
        if trampolines == 1:
            juego.agregar_trampolines()
        t_inicio = time()
        barra2.setCPU(0)
        cerrar = False
    def jugador_doubles(self):
        ser.write(b"0")
        global t_inicio
        global cerrar
        global barras
        barras = 2
        barra2.setCPU(0)
        juego.hacer_matriz()
        if trampolines == 1:
            juego.agregar_trampolines()
        t_inicio = time()
        cerrar = False
    def jugador_practica(self):
        ser.write(b"0")
        global practica
        global cerrar
        global comprobar
        global trampolines
        trampolines = 0
        comprobar = 0
        practica = 1
        juego.hacer_matriz()
        juego.modo_practica()
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
                       font=("Fixedsys", 16),
                       bg="white",
                       command=volver)
        atras.place(x=820, y=25)

        #Labels con descripciones de modos de juego
        descripcion_singles = Label(canvas_modos,
                                    text="Modo Singles es un un tipo de juego en el que participan\n dos jugadores, y cada jugador controla una paleta",
                                    font=("Fixedsys", 20),
                                    bg="black",
                                    fg="white")
        descripcion_singles.place(x=100, y=200)

        descripcion_doubles = Label(canvas_modos,
                                    text="Modo Doubles: a diferencia del Modo Singles, este es un un tipo\n de juego en el que participan dos jugadores, y cada\n jugador controla dos paletas",
                                    font=("Fixedsys", 20),
                                    bg="black",
                                    fg="white")
        descripcion_doubles.place(x=30, y=500)

        lb_doubles = Label(canvas_modos,
                                    text="Modo Doubles",
                                    font=("Fixedsys", 30),
                                    bg="black",
                                    fg="white")
        lb_doubles.place(x=400, y=425)

        lb_singles = Label(canvas_modos,
                                    text="Modo Singles",
                                    font=("Fixedsys", 30),
                                    bg="black",
                                    fg="white")
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
                       font=("Fixedsys", 16),
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
                                  font=("Fixedsys", 17),
                                  bg="black",
                                  fg="white",
                                  justify="left")
        descripcion_juego.place(x=10, y=90)

        descripcion_controles = Label(canvas_instrucciones,
                                      text="Controles: \n \n"
                                           "- Para los modos de un jugador, el usuario va a pode mover su barra para arriba y para abajo con\n"
                                           "Tecla W y Tecla S respectivamente y así no dejar que la bola entre a la zona que se está defendiendo,\n"
                                           "para intentar que el adversario no anote ni acumule puntos, y poder ganar.\n"
                                           "\n- Para los modos de dos jugadores, el jugador de la izquierda moverá su barra para arriba y para abajo\n"
                                           "con las teclas Tecla  W y  Tecla S respectivamente. Por otro lado, el segundo jugador usará las Flecha\n"
                                           "Arriba y Flecha Abajo respectivamente para mover arriba y abajo su barra posicionada al lado derecho\n"
                                           "de la pantalla",
                                      font=("Fixedsys", 17),
                                      bg="black",
                                      fg="white",
                                      justify="left")
        descripcion_controles.place(x=10, y=400)
    def encender_pygame(self):
        pygame.init()
        juego.menu_principal()
    def ventana_practica(self):
        global Fps
        global nivel
        nivel = 1
        Fps = 20

        vprac = Tk()
        vprac.title("PRÁCTICA")
        vprac.minsize(600, 430)
        vprac.maxsize(600, 430)

        pcan = Canvas(vprac, width = 600, height = 430, bg = "black")
        pcan.place(x=-2, y=-2)
        pcan.pack()

        def vlento():
            global Fps
            Fps = 20
            vel.config(text = "Velocidad Actual: Lento")

        def vnormal():
            global Fps
            Fps = 30
            vel.config(text="Velocidad Actual: Normal")

        def vrapida():
            global Fps
            Fps = 35
            vel.config(text="Velocidad Actual: Rapido")

        def blarga():
            global nivel
            nivel = 1
            lar.config(text="Largo de la Barra Actual: Larga")

        def bmedia():
            global nivel
            nivel = 2
            lar.config(text="Largo de la Barra Actual: Mediana")

        def bcorta():
            global nivel
            nivel = 3
            lar.config(text="Largo de la Barra Actual: Corta")

        def salirm():
            vprac.destroy()
            juego.menu_principal()

        def jugar():
            vprac.destroy()
            juego.jugador_practica()

        elige = Label(pcan,
                      text = "Elige la velocidad del juego y el largo de la barra",
                      font=("Fixedsys", 16),
                      bg="black",
                      fg="white")
        elige.place(x = 30, y = 30)

        vel = Label(pcan,
                    text="Velocidad Actual: Lento",
                    font=("Fixedsys", 16),
                    bg="black",
                    fg="white")
        vel.place(x=160, y=90)

        lento = Button(pcan,
                       text="Lento",
                       font=("Fixedsys", 14),
                       bg="white",
                       command = vlento)
        lento.place(x=150, y=130)

        normal = Button(pcan,
                        text="Normal",
                        font=("Fixedsys", 14),
                        bg="white",
                        command=vnormal)
        normal.place(x=250, y=130)

        rapido = Button(pcan,
                        text="Rapido",
                        font=("Fixedsys", 14),
                        bg="white",
                        command=vrapida)
        rapido.place(x=355, y=130)

        lar = Label(pcan,
                    text="Largo de la Barra Actual: Larga",
                    font=("Fixedsys", 16),
                    bg="black",
                    fg="white")
        lar.place(x=120, y=185)

        larga = Button(pcan,
                       text="Larga",
                       font=("Fixedsys", 14),
                       bg="white",
                       command=blarga)
        larga.place(x=150, y=225)

        mediana = Button(pcan,
                         text="Mediana",
                         font=("Fixedsys", 14),
                         bg="white",
                         command=bmedia)
        mediana.place(x=250, y=225)

        corta = Button(pcan,
                       text="Corta",
                       font=("Fixedsys", 14),
                       bg="white",
                       command=bcorta)
        corta.place(x=368, y=225)

        jugar = Button(pcan,
                       text="JUGAR",
                       font=("Fixedsys", 18),
                       bg="white",
                       command=jugar)
        jugar.place(x = 170, y = 310)

        salir = Button(pcan,
                       text="Salir",
                       font=("Fixedsys", 18),
                       bg="white",
                       command = salirm)
        salir.place(x = 320, y = 310)

        vprac.mainloop()

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
        if M[pos [0] + vel[0]][pos[1] + vel[1]] == 33:
            vel = [vel[0], -vel[1]]
            if volumen == 0:
                pygame.mixer.music.load("Blip.wav")
                pygame.mixer.music.play()
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 11:
            if volumen == 0:
                pygame.mixer.music.load("Blip.wav")
                pygame.mixer.music.play()
            vel = [-1, -vel[1]]
            bola.setVelocidad(vel)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 12:
            if volumen == 0:
                pygame.mixer.music.load("Blip.wav")
                pygame.mixer.music.play()
            vel = [0, -vel[1]]
            bola.setVelocidad(vel)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 13:
            if volumen == 0:
                pygame.mixer.music.load("Blip.wav")
                pygame.mixer.music.play()
            vel = [1, -vel[1]]
            bola.setVelocidad(vel)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 41:
            if practica == 1 and barra2.getPuntos() > 9:
                barra1.setNiveles(2)
                if volumen == 0:
                    pygame.mixer.music.load("Anota.wav")
                    pygame.mixer.music.play()
            elif barra2.getPuntos() > 9:
                ser.write(b"0")
                nivel += 1
                if nivel == 2:
                    Fps = 30
                if nivel == 3:
                    Fps = 35
                barra2.setPuntos(0)
                barra1.setPuntos(0)
                juego.hacer_matriz()
                if trampolines == 1:
                    juego.agregar_trampolines()
                pos = [11, 19]
                bola.setPosicion(pos)
                ganador = barra2.getNiveles()
                ganador += 1
                if ganador != 2:
                    if volumen == 0:
                        pygame.mixer.music.load("Nivel.wav")
                        pygame.mixer.music.play()
                barra2.setNiveles(ganador)
                sleep(0.5)
            else:
                if volumen == 0:
                    pygame.mixer.music.load("Anota.wav")
                    pygame.mixer.music.play()
                punto = barra2.getPuntos()
                punto += 1
                if punto == 1:
                    ser.write(b"A")
                if punto == 2:
                    ser.write(b"B")
                if punto == 3:
                    ser.write(b"C")
                if punto == 4:
                    ser.write(b"D")
                if punto == 5:
                    ser.write(b"E")
                if punto == 6:
                    ser.write(b"F")
                if punto == 7:
                    ser.write(b"G")
                if punto == 8:
                    ser.write(b"H")
                if punto == 9:
                    ser.write(b"I")
                if punto == 10:
                    ser.write(b"J")
                barra2.setPuntos(punto)
                bola.setVelocidad([1,1])
                pos = [11, 19]
                bola.setPosicion(pos)
                juego.hacer_matriz()
                if practica == 1:
                    juego.modo_practica()
                if trampolines == 1:
                    juego.agregar_trampolines()
                sleep(0.1)
        if M[pos[0] + vel[0]][pos[1] + vel[1]] == 42:
            if barra1.getPuntos() > 9:
                nivel += 1
                ser.write(b"0")
                if nivel == 2:
                    Fps = 30
                if nivel == 3:
                    Fps = 35
                barra1.setPuntos(0)
                barra2.setPuntos(0)
                juego.hacer_matriz()
                if trampolines == 1:
                    juego.agregar_trampolines()
                pos = [11, 19]
                bola.setPosicion(pos)
                ganador = barra1.getNiveles()
                ganador += 1
                if ganador != 2:
                    if volumen == 0:
                        pygame.mixer.music.load("Nivel.wav")
                        pygame.mixer.music.play()
                barra1.setNiveles(ganador)
                sleep(0.5)
            else:
                if volumen == 0:
                    pygame.mixer.music.load("Anota.wav")
                    pygame.mixer.music.play()
                punto = barra1.getPuntos()
                punto += 1
                if punto == 1:
                    ser.write(b"1")
                if punto == 2:
                    ser.write(b"2")
                if punto == 3:
                    ser.write(b"3")
                if punto == 4:
                    ser.write(b"4")
                if punto == 5:
                    ser.write(b"5")
                if punto == 6:
                    ser.write(b"6")
                if punto == 7:
                    ser.write(b"7")
                if punto == 8:
                    ser.write(b"8")
                if punto == 9:
                    ser.write(b"9")
                if punto == 10:
                    ser.write(b"!")
                barra1.setPuntos(punto)
                bola.setVelocidad([1, 1])
                pos = [11, 19]
                bola.setPosicion(pos)
                juego.hacer_matriz()
                if trampolines == 1:
                    juego.agregar_trampolines()
                sleep(0.1)
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
        pantalla.fill(color1)
        comprobar = 1

    try:
        entrada = str(ser.readline())
        dato = entrada[entrada.index("'") + 1: entrada.index("\\")]
        if (dato == "w") and juego.getMatriz()[0][2] == 31 :
            barra1.moverse("Arriba1")
        if (dato == "s") and juego.getMatriz()[24][2] == 32 :
            barra1.moverse("Abajo1")
        if (dato == "up") and juego.getMatriz()[0][37] == 31 and barra2.getCPU() == 0 and practica != 1:
            barra2.moverse("Arriba2")
        if (dato == "down") and  juego.getMatriz()[24][37] == 32 and barra2.getCPU() == 0 and practica != 1:
            barra2.moverse("Abajo2")
        if (dato == "p"):
            if volumen == 0:
                pygame.mixer.music.load("Pausa.wav")
                pygame.mixer.music.play()
            juego.pausa()
        if(dato == "v"):
            if volumen == 0:
                volumen = 1
            else:
                volumen = 0
        if(dato == "c"):
            juego.cambiarColor()
    except:
        pass

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
    if tecla[pygame.K_UP] and juego.getMatriz()[0][37] == 31 and barra2.getCPU() == 0 and practica != 1:
        barra2.moverse("Arriba2")
    if tecla[pygame.K_DOWN] and juego.getMatriz()[24][37] == 32 and barra2.getCPU() == 0 and practica != 1:
        barra2.moverse("Abajo2")
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_c:
                juego.cambiarColor()
            if evento.key == pygame.K_p:
                if volumen == 0:
                    pygame.mixer.music.load("Pausa.wav")
                    pygame.mixer.music.play()
                juego.pausa()
            if evento.key == pygame.K_v:
                if volumen == 0:
                    volumen = 1
                else:
                    volumen = 0
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
                color = color2
            elif ((n >= 2 and n <= 3) or (n >= 6 and n <= 7) or (n >= 10 and n <= 11) or (n >= 14 and n <= 15) or (n >= 18 and n <= 19) or (n >= 22 and n <= 23)) and m == 19:
                color = color2
            elif (barra1.getPuntos() >= 1 and n == 1 and m == 17) or (barra2.getPuntos() >= 1 and n == 1 and m == 21):
                color = color2
            elif (barra1.getPuntos() >= 2 and n == 1 and m == 15) or (barra2.getPuntos() >= 2 and n == 1 and m == 23):
                color = color2
            elif (barra1.getPuntos() >= 3 and n == 1 and m == 13) or (barra2.getPuntos() >= 3 and n == 1 and m == 25):
                color = color2
            elif (barra1.getPuntos() >= 4 and n == 1 and m == 11) or (barra2.getPuntos() >= 4 and n == 1 and m == 27):
                color = color2
            elif (barra1.getPuntos() >= 5 and n == 1 and m == 9) or (barra2.getPuntos() >= 5 and n == 1 and m == 29):
                color = color2
            elif (barra1.getPuntos() >= 6 and n == 3 and m == 17) or (barra2.getPuntos() >= 6 and n == 3 and m == 21):
                color = color2
            elif (barra1.getPuntos() >= 7 and n == 3 and m == 15) or (barra2.getPuntos() >= 7 and n == 3 and m == 23):
                color = color2
            elif (barra1.getPuntos() >= 8 and n == 3 and m == 13) or (barra2.getPuntos() >= 8 and n == 3 and m == 25):
                color = color2
            elif (barra1.getPuntos() >= 9 and n == 3 and m == 11) or (barra2.getPuntos() >= 9 and n == 3 and m == 27):
                color = color2
            elif (barra1.getPuntos() >= 10 and n == 3 and m == 9) or (barra2.getPuntos() >= 10 and n == 3 and m == 29):
                color = color2
            else:
                color = color1
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
        t_final = time()
        t_total = int(t_final - t_inicio)
        leerpuntuaciones()
        ser.write(b"Z")
        if practica == 1:
            cerrar = True
            pygame.quit()
            juego.encender_pygame()
        elif t_total <= int(p1[2]):
            nueva_puntuacion = 1
            cerrar = True
            pygame.quit()
            juego.nuevaPuntuacion(t_total)
        elif t_total <= int(p2[2]):
            nueva_puntuacion = 2
            cerrar = True
            pygame.quit()
            juego.nuevaPuntuacion(t_total)
        elif t_total <= int(p3[2]):
            nueva_puntuacion = 3
            cerrar = True
            pygame.quit()
            juego.nuevaPuntuacion(t_total)
        else:
            cerrar = True
            pygame.quit()
            juego.ganador()
