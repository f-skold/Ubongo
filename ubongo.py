import sys
import random

import pygame
from pygame.locals import *

class dado:

    def __init__(self):
        self.res = 0

        self.i1 = pygame.image.load('DadoImagenes/i1.png')
        self.i2 = pygame.image.load('DadoImagenes/i2.png')
        self.i3 = pygame.image.load('DadoImagenes/i3.png')
        self.i4 = pygame.image.load('DadoImagenes/i4.png')
        self.i5 = pygame.image.load('DadoImagenes/i5.png')
        self.i6 = pygame.image.load('DadoImagenes/i6.png')

    def dibujarDado(self, res, pan):
        if res == 1:
            pan.blit(self.i1, (17 * an + (an/4), 3 * la))
        elif res == 2:
            pan.blit(self.i2, (17 * an + (an / 4), 3 * la))
        elif res == 3:
            pan.blit(self.i3, (17 * an + (an / 4), 3 * la))
        elif res == 4:
            pan.blit(self.i4, (17 * an + (an / 4), 3 * la))
        elif res == 5:
            pan.blit(self.i5, (17 * an + (an / 4), 3 * la))
        elif res == 6:
            pan.blit(self.i6, (17 * an + (an / 4), 3 * la))

    def tirar(self, pan):
        self.res = random.randint(1,6)
        self.dibujarDado(self.res, pan)

class gema:
    def __init__(self, a, b, e):
        self.x = a
        self.y = b
        self.h = 50
        self.w = 50

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

    def dibujargema(self):
        pygame.draw.ellipse(pantalla, self.color, [self.x + an / 4, self.y + la / 4, self.w, self.h])

class jugador:
    def __init__(self, a, b, e):
        self.x = a
        self.y = b
        self.h = 50
        self.w = 50
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

    def dibujarjugador(self):
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

    for y in range(0, 6):
        pygame.draw.line(pantalla, (92, 38, 7), (0, y * (la)), (dimensiones[0] - 1, y * (la)), 2)
    for x in range(1, 13):
        pygame.draw.line(pantalla, (92, 38, 7), (x * (an), 0), (x * (an), dimensiones[1] - 1), 2)


pygame.init()

dimensiones = [1800, 600]
an = dimensiones[0] / 18
la = dimensiones[1] / 6

pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("TABLERO")

Dado = dado()

gemas = [[0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0]]

players = [jugador(12*an, 1*la, 1) , jugador(13*an, 2*la, 2)]

for y in range(0, 6):
    for x in range(0, 12):
        gemas[y][x] = gema(x * an, y * la, random.randint(1, 6))


while True:
    drawTablero(dimensiones, pantalla)

    for j in range(6):
        for i in range(12):
            if gemas[j][i] != 0:
                gemas[j][i].dibujargema()

    for j in range(len(players)):
        players[j].dibujarjugador()

        if players[j].movidas <= 0:
            players[j].mueve = False

    Dado.dibujarDado(Dado.res, pantalla)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
                players[0].ganargemas(gemas)
            if event.key == K_r:
                players[1].ganargemas(gemas)
            if event.key == K_UP:
                if players[0].mueve == True and players[0].movidas > 0 and players[0].y - la >= 0:
                    players[0].y = players[0].y - la
                    players[0].movidas = players[0].movidas - 1
            if event.key == K_DOWN:
                if players[0].mueve == True and players[0].movidas > 0 and players[0].y + la <= la*6:
                    players[0].y = players[0].y + la
                    players[0].movidas = players[0].movidas - 1
            if event.key == K_w:
                if players[1].mueve == True and players[1].movidas > 0 and players[1].y - la >= 0:
                    players[1].y = players[1].y - la
                    players[1].movidas = players[1].movidas - 1
            if event.key == K_s:
                if players[1].mueve == True and players[1].movidas > 0 and players[1].y + la <= la*6:
                    players[1].y = players[1].y + la
                    players[1].movidas = players[1].movidas - 1
            if event.key == K_d:
                Dado.tirar(pantalla)

        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
