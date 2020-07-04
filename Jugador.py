from DadosyGemas import *

class jugador:
    def __init__(self, a, b, e):
        self.x = a
        self.y = b
        self.h = 30
        self.w = 30
        self.mueve = True
        self.movidas = 0
        self.capacidadRecoleccion = 0
        self.gemasganadas = [0,0,0,0,0,0]

        if e == 1:
            self.color = (132, 61, 9)
        elif e == 2:
            self.color = (246, 183, 137)
        elif e == 3:
            self.color = (233, 221, 212)
        elif e == 3:
            self.color = (33, 32, 32)

    def creacionDeFichasDeLosJugadores(self):
        players = [jugador(12 * an, 1 * la, 1), jugador(13 * an, 2 * la, 2)]
        return players

    def dibujarjugador(self, pantalla):
        pygame.draw.ellipse(pantalla, self.color, [self.x + an / 4, self.y + la / 4, self.w, self.h])

    def ganargemas(self, gemas, matGemas):
        gem = gemas
        f = 0
        for i in range(11, -1, -1):
            if f == 2:
                break
            if gemas[int(self.y / la)][i] != 0:
                self.gemasganadas[matGemas[int(self.y/la)][i]-1]+=1
                gemas[int(self.y / la)][i] = 0
                f = f + 1
                
                
    def getGemasGanadas(self):
        return self.gemasganadas
