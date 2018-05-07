import pygame as pygame

cerrar = False

filas = 25
columnas = 40

negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.init()

pantalla = pygame.display.set_mode((800, 500))
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
                else:
                    self.M[n][m] = 0
    def getMatriz(self):
        return self.M
    def setMatriz(self, nuevo):
        self.M = nuevo

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
    def moverse(self, direccion):
        M = juego.getMatriz()
        i = 0
        if direccion == "Arriba1":
            while i != len(M[0]):
                if M[i][3] == 1:
                    M[i - 1][3] = 1
                    M[i + 9][3] = 0
                    juego.setMatriz(M)
                    break
                else:
                    i += 1

juego = Juego([])
barra1 = Barras(3, 0, 0, [2,3], 0, 4, 0)

while not cerrar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cerrar = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                barra1.moverse("Arriba1")

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
            pygame.draw.rect(pantalla, color, [x, y, 20, 20])
            x += 20
            m += 1
        x = 0
        y += 20
        n += 1
        m = 0
    pygame.display.update()
