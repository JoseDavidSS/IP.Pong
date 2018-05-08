import pygame
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
        canvas = Canvas(ventana, width=1080, height=720, bg="black")
        canvas.place(x=-2, y=-2)
        canvas.pack()

        #Funciones que llaman a los otros métodos de la clase con instancias
        def ventana_un_jugador_aux():
            ventana.destroy()
            Instancia_Juego.ventana_un_jugador()

        def ventana_dos_jugadores_aux():
            ventana.withdraw()
            Instancia_Juego.ventana_dos_jugadores()

        def ventana_instrucciones_aux():
            ventana.withdraw()
            Instancia_Juego.ventana_instrucciones()


        # Boton para iniciar partida de un jugador
        un_jugador = Button(canvas,
                                 text="Un jugador",
                                 font=("Arial", 20),
                                 width=14,
                                 bg="white",
                                 command = ventana_un_jugador_aux)
        un_jugador.place(x=425, y=300)

        # Boton para iniciar partida de dos jugadores
        dos_jugadores = Button(canvas,
                                 text="Dos Jugadores",
                                 font=("Arial", 20),
                               width=14,
                                 bg="white",
                                 command = ventana_dos_jugadores_aux)
        dos_jugadores.place(x=425, y=400)

        # Boton para ir a ventana de instrucciones
        bt_instrucciones = Button(canvas,
                                 text="Instrucciones",
                                 font=("Arial", 20),
                                width=14,
                                 bg="white",
                                 command = ventana_instrucciones_aux)
        bt_instrucciones.place(x=425, y=600)

        #Labels
        titulo = Label(canvas,
                                    text="PONG",
                                    font=("Arial",78),
                                    bg="black",
                                    fg="white")
        titulo.place(x=390,y=15)

        # Fin del loop
        ventana.mainloop()

    def ventana_un_jugador(self):
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
                    pygame.quit()
                print(event)
            pygame.display.update()
            clock.tick(60)

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
            Instancia_Juego.menu_principal()

        def modo_singles_aux():
            ventana_dos_jugadores.destroy()
            Instancia_Juego.modo_singles()

        def modo_doubles_aux():
            ventana_dos_jugadores.destroy()
            Instancia_Juego.modo_doubles()

        #Botón para volver al menú principal
        atras = Button(canvas_dos_jugadores,
                                 text="Volver al Menú Principal",
                                 font=("Arial", 16),
                                 bg="white",
                                 command=volver)
        atras.place(x=820, y=25)

        #Botón para jugar modo singles
        singles = Button(canvas_dos_jugadores,
                                 text="Jugar modo Singles",
                                 font=("Arial", 20),
                                 bg="white",
                                 command=modo_singles_aux)
        singles.place(x=420, y=300)

        #Botón para jugar modo doubles
        doubles = Button(canvas_dos_jugadores,
                                 text="Jugar modo Doubles",
                                 font=("Arial", 20),
                                 bg="white",
                                 command=modo_doubles_aux)
        doubles.place(x=420, y=600)

        #Labels de descripciones de modos de juego
        descripcion_singles = Label(canvas_dos_jugadores,
                                    text="Modo Singles es un un tipo de juego en el que participan\n dos jugadores, y cada jugador controla una paleta",
                                    font=("Arial",20),
                                    bg="black",
                                    fg="white")
        descripcion_singles.place(x=200,y=200)

        descripcion_doubles = Label(canvas_dos_jugadores,
                                    text="Modo Doubles: a diferencia del Modo Singles, este es un un tipo de juego\n en el que participan dos jugadores, y cada jugador controla dos paletas",
                                    font=("Arial",20),
                                    bg="black",
                                    fg="white")
        descripcion_doubles.place(x=95,y=500)

    def modo_singles(self):
        ColorUno = (0, 140, 60)
        ColorDos = pygame.Color(255, 120, 9)
        pygame.init()
        ventana_singles = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Modo Singles")
        clock = pygame.time.Clock()

        self.crashed = False
        while not self.crashed:
            ventana_singles.fill(ColorDos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                    pygame.quit()
                print(event)
            pygame.display.update()
            clock.tick(60)

    def modo_doubles(self):
        ColorUno = (0, 140, 60)
        ColorDos = pygame.Color(255, 120, 9)
        pygame.init()
        ventana = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Modo Doubles")
        clock = pygame.time.Clock()

        crashed = False
        while not crashed:
            ventana.fill(ColorDos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    pygame.quit()
                print(event)
            pygame.display.update()
            clock.tick(60)

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
            Instancia_Juego.menu_principal()

        #Botón para volver al menú principal
        atras = Button(canvas_instrucciones,
                                 text="Volver al Menú Principal",
                                 font=("Arial", 16),
                                 bg="white",
                                 command=volver)
        atras.place(x=820, y=25)

        #Labels de descripciones de modos de juego
        descripcion_juego = Label(canvas_instrucciones,
                                    text="Descripción: \n \n"
                                         "Pong es un juego de deportes en dos dimensiones que simula un tenis de mesa. \n"
                                         "El jugador controla en el juego una paleta moviéndola verticalmente en la parte izquierda de la pantalla,\n"
                                         "y puede competir tanto contra un oponente controlado por computadora, como con otro jugador\n"
                                         "humano que controla una segunda paleta en la parte opuesta. Los jugadores pueden usar las paletas\n"
                                         "para pegarle a la pelota hacia un lado u otro. El objetivo consiste en que uno de los jugadores consiga \n"
                                         "más puntos que el oponente al finalizar el juego. Estos puntos se obtienen cuando el jugador adversario \n"
                                         "falla al devolver la pelota.",
                                    font=("Arial",17),
                                    bg="black",
                                    fg="white",
                                    justify="left")
        descripcion_juego.place(x=20,y=90)

#Clase de Barras
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

#Clase de Bola
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

Instancia_Juego = Juego("matriz")
Instancia_Juego. menu_principal()