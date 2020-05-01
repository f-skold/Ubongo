import pygame
from random import randint

class CFigura:
    x = 0
    y = 0
    _id = 0
    col = (0, 0, 0)
    image = 0

    def __init__(self, x, y, n, filename):
        self.x = x
        self.y = y
        self._id = n
        self.imagen(filename, True)
        if self._id == 4 or self._id == 6:
            self.col = self.image.get_at((51,25))
        else:
            self.col = self.image.get_at((0,0))
        
    def imagen(self, filename, transparent=False):
        self.image = pygame.image.load(filename)
        self.image = self.image.convert()
        if transparent:
            color = self.image.get_at((0,0))
            self.image.set_colorkey((255,255,255), pygame.RLEACCEL)

    def cargarImg(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def rotarImg(self, angulo):
        if angulo == 0:
            self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = pygame.transform.rotate(self.image, -90)
        
    def getId(self):
        return self._id

    def getCol(self):
        return self.col

    def setPos(self, x, y):
        self.x = x
        self.y = y
        
    def getImage(self):
        return self.image

class Escenarios:
    # ESCENARIOS
    #3 FICHAS
    def DibujarPlantilla1(self, surface):
        color = (255, 250, 245)
        x = 600
        y = 0

        #DIBUJAR TABLERO DE JUGADOR PERSONA
        #Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x+50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x+100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x+150, y), (50, 50)], 1)
        #Fila 2
        pygame.draw.rect(surface, color, [(x + 50, y+50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y+50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        #Fila 3
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 100), (50, 50)], 1)
        #Fila 4
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        # Fila 1
        y = 400
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)

    # 3 FICHAS
    def DibujarPlantilla2(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)

        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x + 100, y + 250), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x + 100, y + 250), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla3(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 250), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 250), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla4(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0

        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 150), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 150), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla5(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla6(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 200), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 200), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla7(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x, y + 250), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        # Fila 5
        pygame.draw.rect(surface, color, [(x, y + 200), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 200), (50, 50)], 1)
        # Fila 6
        pygame.draw.rect(surface, color, [(x, y + 250), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 250), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla8(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)

    # 4 FICHAS
    def DibujarPlantilla9(self,surface):
        color = (255, 250, 245)
        x = 600
        y = 0
        # DIBUJAR TABLERO DE JUGADOR PERSONA
        # Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 150), (50, 50)], 1)

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        y = 400
        # Fila 1
        pygame.draw.rect(surface, color, [(x, y), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y), (50, 50)], 1)
        # Fila 2
        pygame.draw.rect(surface, color, [(x, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 50), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 50), (50, 50)], 1)
        # Fila 3
        pygame.draw.rect(surface, color, [(x, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 100), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 100), (50, 50)], 1)
        # Fila 4
        pygame.draw.rect(surface, color, [(x, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 50, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 100, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 150, y + 150), (50, 50)], 1)
        pygame.draw.rect(surface, color, [(x + 200, y + 150), (50, 50)], 1)
