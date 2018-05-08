import pygame as pygame

cerrar = False

filas = 25
columnas = 40

largo_pantalla = 1080
ancho_pantalla = 720

largo_cuadro = largo_pantalla // columnas
ancho_cuadro = ancho_pantalla // filas

negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.init()

pantalla = pygame.display.set_mode((largo_pantalla, ancho_pantalla))
pygame.display.set_caption("PONG")
pantalla.fill((10, 10, 10))

class Juego:
    def __init__(self, M):
        self.M = M
        for n in range(filas):
            self.M.append([])
            for m in range(columnas):
                self.M[n].append(0)
        for n in range(filas):
            for m in range(columnas):
                if n >= 7 and n <= 15 and m == 3:
                    self.M[n][m] = 1
                elif n >= 7 and n <= 15 and m == 36:
                    self.M[n][m] = 1
                elif n == 11 and m == 19:
                    self.M[n][m] = 2
                elif n == 0 or n == 24:
                    self.M[n][m] = 3
                elif m == 0 or m == 39:
                    self.M[n][m] = 4
                else:
                    self.M[n][m] = 0
    def getMatriz(self):
        return self.M
    def setMatriz(self, nuevo):
        self.M = nuevo

class Bola:
    def __init__(self):
        self.posicion = [11, 19]
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
    def movimiento(self):
        M = juego.getMatriz()
        pos = bola.getPosicion()
        M[pos[0]][pos[1]] = 0
        M[pos[0] + 1][pos[1] + 1] = 2
        pos = [pos[0] + 1, pos[1] + 1]
        bola.setPosicion(pos)
        juego.setMatriz(M)

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
    def setLargo(self, nuevo):
        self.largo = nuevo
    def setPosicion(self, nuevo):
        self.posicion = nuevo
    def setPuntos(self, nuevo):
        self.puntos = nuevo
    def setVelocidad(self, nuevo):
        self.velocidad = nuevo
    def moverse(self, direccion):
        M = juego.getMatriz()
        i = 0
        if direccion == "Arriba1":
            while i != len(M[0]):
                if M[i][3] == 1:
                    M[i - 1][3] = 1
                    M[i + 8][3] = 0
                    M[24][3] = 3
                    juego.setMatriz(M)
                    break
                else:
                    i += 1
        elif direccion == "Abajo1":
            while i != len(M[0]):
                if M[i][3] == 1:
                    M[i][3] = 0
                    M[i + 9][3] = 1
                    M[0][3] = 3
                    juego.setMatriz(M)
                    break
                else:
                    i += 1
        elif direccion == "Arriba2":
            while i != len(M[0]):
                if M[i][36] == 1:
                    M[i - 1][36] = 1
                    M[i + 8][36] = 0
                    M[24][36] = 3
                    juego.setMatriz(M)
                    break
                else:
                    i += 1
        elif direccion == "Abajo2":
            while i != len(M[0]):
                if M[i][36] == 1:
                    M[i][36] = 0
                    M[i + 9][36] = 1
                    M[0][36] = 3
                    juego.setMatriz(M)
                    break
                else:
                    i += 1

juego = Juego([])
barra1 = Barras(3, 0, 0, [2,3], 0, 4, 0)
barra2 = Barras(3, 0, 0, [2,3], 0, 4, 0)
bola = Bola()
contador = 150

while not cerrar:
    control_movimiento = pygame.time.get_ticks() // 10
    tecla = pygame.key.get_pressed()
    bola.movimiento()
    if contador == control_movimiento:
        contador += 5
        if tecla[pygame.K_UP] and juego.getMatriz()[0][3] == 3:
            barra1.moverse("Arriba1")
        if tecla[pygame.K_DOWN] and juego.getMatriz()[24][3] == 3:
            barra1.moverse("Abajo1")
        if tecla[pygame.K_w] and juego.getMatriz()[0][36] == 3:
            barra1.moverse("Arriba2")
        if tecla[pygame.K_s] and juego.getMatriz()[24][36] == 3:
            barra1.moverse("Abajo2")
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cerrar = True

    x = 0
    y = 0
    n = 0
    m = 0
    while n != filas:
        while m != columnas:
            if juego.getMatriz()[n][m] == 1:
                color = blanco
            elif juego.getMatriz()[n][m] == 2:
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
