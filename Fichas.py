import pygame

# import backtracking_ubongo


class CFigura:
    x = 0
    y = 0
    ini_x = 0
    ini_y = 0
    _id = 0
    col = (0, 0, 0)
    image = None
    mat = []
    ma_pos = []

    def __init__(self, x, y, n, filename):
        self.x = x
        self.y = y
        self.ini_x = self.x
        self.ini_y = self.y

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
                    self.mat[i][j] = self._id

    def imagen(self, filename, transparent=False):
        self.image = pygame.image.load(filename)
        self.image = self.image.convert()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        if transparent:
            # color = self.image.get_at((0, 0))
            self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)

    def cargarImg(self, screen):
        if self.image is None:
            filename = f"Fichas/Ficha{self._id}.png"
            self.imagen(filename, transparent=True)

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
        self.x -= self.x % 50
        self.y -= self.y % 50

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

    # measured in pixels
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getMat(self):
        return self.mat

    def getMatPos(self):
        return self.ma_pos

    def setMatPos(self, pos):
        self.ma_pos = pos

    def setIniPos(self):
        self.x = self.ini_x
        self.y = self.ini_y
