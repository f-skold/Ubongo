import random
from FichasyTableros import *

# Parametros para dibujar el tablero
dimensiones = [1000, 300]
an = dimensiones[0] / 18
la = dimensiones[1] / 6

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

    def getRes(self):
        return self.res

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

    def inicializarGemas(self):
        gemas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        return gemas
    
    def getGemas(self,i,j):
        return self.gemas[i][j]

