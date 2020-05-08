import sys
import random

import pygame
from pygame.locals import *


class dado:

    def __init__(self):
        self.res = 0

        self.i1 = pygame.image.load(r'DadoImagenes/i1.png')
        self.i2 = pygame.image.load(r'DadoImagenes/i2.png')
        self.i3 = pygame.image.load(r'DadoImagenes/i3.png')
        self.i4 = pygame.image.load(r'DadoImagenes/i4.png')
        self.i5 = pygame.image.load(r'DadoImagenes/i5.png')
        self.i6 = pygame.image.load(r'DadoImagenes/i6.png')

    def dibujarDado(self, res, pan):
        if res == 1:
            pan.blit(self.i1, (16 * an + (an / 4), 3 * la))
        elif res == 2:
            pan.blit(self.i2, (16 * an + (an / 4), 3 * la))
        elif res == 3:
            pan.blit(self.i3, (16 * an + (an / 4), 3 * la))
        elif res == 4:
            pan.blit(self.i4, (16 * an + (an / 4), 3 * la))
        elif res == 5:
            pan.blit(self.i5, (16 * an + (an / 4), 3 * la))
        elif res == 6:
            pan.blit(self.i6, (16 * an + (an / 4), 3 * la))

    def tirar(self, pan):
        self.res = random.randint(1, 6)
        self.dibujarDado(self.res, pan)


class gema:
    def __init__(self, a, b, e):
        self.x = a
        self.y = b
        self.h = 30
        self.w = 30

        if e == 1:
            self.color = (255, 0, 0)
        elif e == 2:
            self.color = (0, 0, 255)
        elif e == 3:
            self.color = (52, 234, 17)
        elif e == 4:
            self.color = (255, 255, 0)
        elif e == 5:
            self.color = (255, 147, 0)
        elif e == 6:
            self.color = (183, 0, 255)

    def dibujargema(self, pantalla):
        pygame.draw.ellipse(pantalla, self.color, [self.x + an / 4, self.y + la / 4, self.w, self.h])


class jugador:
    def __init__(self, a, b, e):
        self.x = a
        self.y = b
        self.h = 30
        self.w = 30
        self.mueve = True
        self.movidas = 3
        self.gemasganadas = []

        if e == 1:
            self.color = (132, 61, 9)
        elif e == 2:
            self.color = (246, 183, 137)
        elif e == 3:
            self.color = (233, 221, 212)
        elif e == 3:
            self.color = (33, 32, 32)

    def dibujarjugador(self, pantalla):
        pygame.draw.ellipse(pantalla, self.color, [self.x + an / 4, self.y + la / 4, self.w, self.h])

    def ganargemas(self, gemas):
        f = 0
        for i in range(11, -1, -1):
            if f == 2:
                break
            if gemas[int(self.y / la)][i] != 0:
                self.gemasganadas.append(gemas[int(self.y / la)][i])
                gemas[int(self.y / la)][i] = 0
                f = f + 1


def drawTablero(dimensiones, pantalla):
    pygame.draw.rect(pantalla, (248, 190, 38), [0, 0, dimensiones[0], dimensiones[1]])
    pygame.draw.rect(pantalla, (128, 128, 0), [12 * (an), 0, dimensiones[0] - (an), dimensiones[1]])
    pygame.draw.rect(pantalla, (128, 55, 0), [16 * (an), 0, dimensiones[0] - (an), dimensiones[1]])

    for y in range(0, 7):
        pygame.draw.line(pantalla, (92, 38, 7), (0, y * (la)), (dimensiones[0] - 1, y * (la)), 2)
    for x in range(1, 13):
        pygame.draw.line(pantalla, (92, 38, 7), (x * (an), 0), (x * (an), dimensiones[1] - 1), 2)


class CFigura:
    x = 0
    y = 0
    _id = 0
    col = (0, 0, 0)
    image = 0
    mat = []

    def __init__(self, x, y, n, filename):
        self.x = x
        self.y = y
        self._id = n
        self.imagen(filename, True)
        if self._id == 4 or self._id == 6 or self._id == 10:
            self.col = self.image.get_at((51, 25))
        else:
            self.col = self.image.get_at((0, 0))
        self.formaMatriz()

    def formaMatriz(self):
        ancho, alto = self.image.get_rect().size
        self.mat = [[-1 for i in range(ancho // 50)] for j in range(alto // 50)]
        for i in range(0, alto // 50):
            for j in range(0, ancho // 50):
                pixelcol = self.image.get_at((j * 50, i * 50))
                if pixelcol == self.col:
                    self.mat[i][j] = 1
        print(self._id)

    def imagen(self, filename, transparent=False):
        self.image = pygame.image.load(filename)
        self.image = self.image.convert()
        if transparent:
            color = self.image.get_at((0, 0))
            self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)

    def cargarImg(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def rotarImg(self, angulo):
        if angulo == 0:
            self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = pygame.transform.rotate(self.image, -90)

    def voltearImg(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def reescalarImg(self):
        if self._id == 1:
            self.image = pygame.transform.scale(self.image, (150, 50))

    def acomodarImg(self):
        self.x -= (self.x % 50)
        self.y -= (self.y % 50)

    def getId(self):
        return self._id

    def getCol(self):
        return self.col

    def getPos(self):
        return self.x, self.y

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getImage(self):
        return self.image

    def getWidth(self):
        self.width = self.image.get_width()
        return self.width

    def getHeight(self):
        self.height = self.image.get_height()
        return self.height

    def getMat(self):
        return self.mat


class Plantilla:
    # ESCENARIOS

    Figuras = []
    ma_vali = []
    color = (0, 0, 0)
    pos = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Figuras = [
            CFigura(x, (350), 1, "Fichas/Ficha1.png"),
            CFigura(x, (450), 2, "Fichas/Ficha2.png"),
            CFigura(x, (500), 3, "Fichas/Ficha3.png"),
            CFigura(x, (350), 4, "Fichas/Ficha4.png"),
            CFigura(x, (400), 5, "Fichas/Ficha5.png"),
            CFigura(x, (550), 6, "Fichas/Ficha6.png"),
            CFigura(x, (350), 7, "Fichas/Ficha7.png"),
            CFigura(x, (450), 8, "Fichas/Ficha8.png"),
            CFigura(x, (500), 9, "Fichas/Ficha9.png"),
            CFigura(x, (350), 10, "Fichas/Ficha10.png"),
            CFigura(x, (400), 11, "Fichas/Ficha11.png"),
            CFigura(x, (550), 12, "Fichas/Ficha12.png")]

    def colocar(self, piez_x, piez_y, aux):
        n_col = len(self.ma_vali[0])
        n_fil = len(self.ma_vali)
        x = piez_x - self.x
        y = piez_y - self.y
        aux.formaMatriz()
        aux_mat = aux.getMat()

        for f in range(len(aux_mat)):
            for c in range(len(aux_mat[f])):
                if aux_mat[f][c] != -1:
                    self.ma_vali[f + (y // 50)][c + (x // 50)] = aux_mat[f][c]

    def getMat(self):
        return self.ma_vali

    # 3 Fichas
    def DibujarPlantilla1(self, surface, x, y):
        self.color = (255, 255, 255)
        self.x = x
        # x = 600
        # y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x+50, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x+100, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x+150, y), (50, 50)])
        ##Fila 2
        # pygame.draw.rect(surface, color, [(x + 50, y+50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y+50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)])
        ##Fila 3
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 200, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        # Fila 1
        self.y = y
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, 0, 0, -1],
                            [-1, 0, 0, 0, -1],
                            [-1, 0, 0, 0, 0],
                            [-1, -1, 0, 0, -1]]

    # 3 FICHAS
    def DibujarPlantilla2(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)])

        # Fila 2
        # pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # Fila 5
        # pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)])
        # Fila 6
        # pygame.draw.rect(surface, color, [(x + 100, y + 250), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)])
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 250), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, -1],
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0],
                            [-1, -1, 0],
                            [-1, -1, 0]]

    # 4 FICHAS
    def DibujarPlantilla3(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        # Fila 5
        # pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)])
        # Fila 6
        # pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 250), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)])
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 250), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [-1, 0, 0, 0],
                            [-1, 0, 0, -1],
                            [-1, 0, 0, -1]]

    # 4 FICHAS
    def DibujarPlantilla4(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, self.color, [(self.x + 50, y), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, self.color, [(self.x, y + 50), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 50, y + 50), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, self.color, [(self.x, y + 100), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 150, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, self.color, [(self.x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 150, y + 150), (50, 50)])
        # pygame.draw.rect(surface, self.color, [(self.x + 200, y + 150), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 150), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, 0, 0, -1, -1],
                            [0, 0, 0, -1, -1],
                            [0, 0, 0, 0, -1],
                            [-1, 0, 0, 0, 0, ]]

    # 4 FICHAS
    def DibujarPlantilla5(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)])
        # Fila 5
        # pygame.draw.rect(surface, color, [(x, y + 200), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 200), (50, 50)])
        # Fila 6
        # pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 200), (50, 50)])
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, -1, 0, 0],
                            [-1, -1, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [-1, 0, -1, -1]]

    # 4 FICHAS
    def DibujarPlantilla6(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)])
        # Fila 5
        # pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 200), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 200), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, -1, 0, 0],
                            [-1, -1, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [-1, 0, 0, 0]]

    # 4 FICHAS
    def DibujarPlantilla7(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)])
        # Fila 5
        # pygame.draw.rect(surface, color, [(x, y + 200), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)])
        # Fila 6
        # pygame.draw.rect(surface, color, [(x, y + 250), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 200), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)])
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 250), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, 0, 0, -1],
                            [-1, 0, 0, 0],
                            [-1, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, -1, -1],
                            [0, 0, -1, -1]]

    # 4 FICHAS
    def DibujarPlantilla8(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [-1, 0, 0, 0],
                            [-1, 0, 0, 0]]

    # 4 FICHAS
    def DibujarPlantilla9(self, surface, x, y):
        self.color = (33, 33, 33)
        self.x = x
        # y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        # pygame.draw.rect(surface, color, [(x, y), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)])
        # Fila 2
        # pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 200, y + 50), (50, 50)])
        # Fila 3
        # pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 200, y + 100), (50, 50)])
        # Fila 4
        # pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)])
        # pygame.draw.rect(surface, color, [(x + 200, y + 150), (50, 50)])

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        self.y = y
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)])
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 50), (50, 50)])
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 100), (50, 50)])
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)])
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 150), (50, 50)])

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, -1, -1, -1],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]

    def getFiguras(self):
        return self.Figuras

    def cargarFiguras(self, surface, cara, nplantilla):
        if cara == 0:
            self.Figuras[3].cargarImg(surface)
            self.Figuras[5].cargarImg(surface)
            self.Figuras[8].cargarImg(surface)
        elif cara == 1:
            self.Figuras[9].cargarImg(surface)
            self.Figuras[5].cargarImg(surface)
            self.Figuras[0].cargarImg(surface)
        elif cara == 2:
            self.Figuras[0].cargarImg(surface)
            self.Figuras[2].cargarImg(surface)
            self.Figuras[4].cargarImg(surface)
        elif cara == 3:
            self.Figuras[1].cargarImg(surface)
            self.Figuras[7].cargarImg(surface)
            self.Figuras[5].cargarImg(surface)
        elif cara == 4:
            self.Figuras[6].cargarImg(surface)
            self.Figuras[9].cargarImg(surface)
            self.Figuras[5].cargarImg(surface)
        elif cara == 5:
            self.Figuras[9].cargarImg(surface)
            self.Figuras[11].cargarImg(surface)
            self.Figuras[3].cargarImg(surface)


# Parametros para dibujar el tablero
dimensiones = [1000, 300]
an = dimensiones[0] / 18
la = dimensiones[1] / 6


def main():
    # Booleano que controla el while principal
    running = True

    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption('Ubongo!!!')

    screen = pygame.display

    # Tamaño de la pantalla
    xs = 1000
    ys = 900

    # Datos del tablero
    Dado = dado()

    gemas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    players = [jugador(12 * an, 1 * la, 1), jugador(13 * an, 2 * la, 2)]

    for y in range(0, 6):
        for x in range(0, 12):
            gemas[y][x] = gema(x * an, y * la, random.randint(1, 6))

    #

    # Superfice que se toma
    surface = screen.set_mode([xs, ys])

    pygame.display.flip()

    # Reloj
    reloj = pygame.time.Clock()

    # Se crea la lista de Escenarios
    Esc = Plantilla(600, 0)
    Esc2 = Plantilla(100, 0)
    # Variables controladoras
    # X y Y sirven para obtener la posicion del raton
    x = 0
    y = 0
    # Bool que activa o desactiva el movimiento
    activate = False

    # aux -> Tomará los valores de la Figura seleccionada
    aux = 0

    # bucle infinito
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Si se apreta una tecla
            elif event.type == pygame.KEYDOWN:
                # si la tecla es "d" rota en sentido horario
                if event.key == pygame.K_d and aux != 0:
                    aux.rotarImg(1)

                # si la tecla es "a" rota es sentido anti-horario
                if event.key == pygame.K_a and aux != 0:
                    aux.rotarImg(0)

                # Si la tecla es "q" la imgaen se voltea
                if event.key == pygame.K_q and aux != 0:
                    aux.voltearImg()

                # teclas tablero
                if event.key == K_e:
                    players[0].ganargemas(gemas)
                if event.key == K_r:
                    players[1].ganargemas(gemas)
                if event.key == K_UP:
                    if players[0].mueve == True and players[0].movidas > 0 and players[0].y - la >= 0:
                        players[0].y = players[0].y - la
                        players[0].movidas = players[0].movidas - 1
                if event.key == K_DOWN:
                    if players[0].mueve == True and players[0].movidas > 0 and players[0].y + la <= la * 6:
                        players[0].y = players[0].y + la
                        players[0].movidas = players[0].movidas - 1
                if event.key == K_w:
                    if players[1].mueve == True and players[1].movidas > 0 and players[1].y - la >= 0:
                        players[1].y = players[1].y - la
                        players[1].movidas = players[1].movidas - 1
                if event.key == K_s:
                    if players[1].mueve == True and players[1].movidas > 0 and players[1].y + la <= la * 6:
                        players[1].y = players[1].y + la
                        players[1].movidas = players[1].movidas - 1
                if event.key == K_x:
                    Dado.tirar(surface)

            # Si se apreta un boton del mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # si el boton es izquierdo
                if event.button == pygame.BUTTON_LEFT:
                    pixel = list(surface.get_at((x, y)))
                    # se busca la figura que coincida con la pos del cursor
                    for i in range(len(Esc.getFiguras())):
                        if pixel == list(Esc.getFiguras()[i].getCol()):
                            # se activa el movimiento
                            activate = True
                            aux = Esc.getFiguras()[i]


                # si el boton es derecho
                elif event.button == pygame.BUTTON_RIGHT:
                    # se cancela el movimiento
                    activate = False
                    # obtener la posicion del mouse
                    posmouse = pygame.mouse.get_pos()
                    if aux != 0:
                        aux.acomodarImg()
                        actualX, actualY = aux.getPos()
                        Esc.colocar(actualX, actualY, aux)
                    aux = 0

        # FPS fijados en 20
        reloj.tick(20)
        x, y = pygame.mouse.get_pos()

        # Cambio de pos de la figura seleccionada
        if activate:
            aux.setPos(x, y)

        origenPlantilla = 240

        surface.fill((255, 139, 129))

        Esc2.DibujarPlantilla1(surface, origenPlantilla, 350)
        Esc.DibujarPlantilla2(surface, origenPlantilla + 500, 350)

        # para tablero
        drawTablero(dimensiones, surface)

        # Para el tablero

        for j in range(6):
            for i in range(12):
                if gemas[j][i] != 0:
                    gemas[j][i].dibujargema(surface)

        for j in range(len(players)):
            players[j].dibujarjugador(surface)

            if players[j].movidas <= 0:
                players[j].mueve = False

        #

        Dado.dibujarDado(Dado.res, surface)

        # Se cargan todas las figuras
        Esc2.cargarFiguras(surface, 1, 0)
        Esc.cargarFiguras(surface, 2, 0)

        pygame.draw.line(surface, (92, 38, 7), (dimensiones[0] / 2, dimensiones[1]), (dimensiones[0] / 2, 900), 2)

        screen.update()


main()