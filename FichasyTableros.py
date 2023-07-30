from random import randint

import pygame

import backtracking_ubongo
import Fichas


class Plantilla:
    # ESCENARIOS

    Figuras = []
    ma_vali = []
    color = (0, 0, 0)
    pos = (0, 0)
    tabla_pc = []
    piezas = []

    def __init__(self, x, y):
        # self.x = x
        self.y = 250

        # old array was 1-12 at 0 based array
        self.Figuras = [
            Fichas.CFigura(100, (300), 1, "Fichas/Ficha1.png"),
            Fichas.CFigura(100, (350), 2, "Fichas/Ficha2.png"),
            Fichas.CFigura(100, (400), 3, "Fichas/Ficha3.png"),
            Fichas.CFigura(100, (450), 4, "Fichas/Ficha4.png"),
            Fichas.CFigura(100, (500), 5, "Fichas/Ficha5.png"),
            Fichas.CFigura(100, (550), 6, "Fichas/Ficha6.png"),
            Fichas.CFigura(300, (300), 7, "Fichas/Ficha7.png"),
            Fichas.CFigura(300, (350), 8, "Fichas/Ficha8.png"),
            Fichas.CFigura(300, (400), 9, "Fichas/Ficha9.png"),
            Fichas.CFigura(300, (450), 10, "Fichas/Ficha10.png"),
            Fichas.CFigura(300, (500), 11, "Fichas/Ficha11.png"),
            Fichas.CFigura(300, (550), 12, "Fichas/Ficha12.png"),
        ]

    def colocar(self, piez_x, piez_y, aux):
        n_col = len(self.ma_vali[0])
        n_fil = len(self.ma_vali)
        self.mostrarMatVali()
        pos = []
        aux.formaMatriz()
        aux_mat = aux.getMat()
        if (
            piez_x >= self.x
            and piez_x + len(aux_mat[0]) * 50 <= self.x + n_col * 50
            and piez_y >= self.y
            and piez_y + len(aux_mat) * 50 <= self.y + n_fil * 50
        ):
            x = (piez_x - self.x) // 50
            y = (piez_y - self.y) // 50
            for f in range(len(aux_mat)):
                for c in range(len(aux_mat[f])):
                    if aux_mat[f][c] != -1:
                        if self.ma_vali[f + y][c + x] == 0 or self.ma_vali[f + y][c + x] == aux.getId():
                            pos.append([f + y, c + x])
                        else:
                            self.mostrarMatVali()
                            # retorna false cuando la pieza se quiere sobreponer a otra
                            return False
            # Vacia la posicion anterior cuando la pieza cambió de posición dentro
            for i in range(len(aux.getMatPos())):
                if self.ma_vali[aux.getMatPos()[i][0]][aux.getMatPos()[i][1]] == aux.getId():
                    self.ma_vali[aux.getMatPos()[i][0]][aux.getMatPos()[i][1]] = 0
            # Llena en la nueva posición
            for i in range(len(pos)):
                self.ma_vali[pos[i][0]][pos[i][1]] = aux.getId()
            aux.setMatPos(pos)

            # retorna True cuando la pieza entra en la plantilla sin ponerse encima de otra pieza
            self.mostrarMatVali()
            return True
        else:
            # Vacia la posicion anterior cuando la pieza se colocó afuera
            actual_pos = aux.getMatPos()
            for i in range(len(actual_pos)):
                self.ma_vali[actual_pos[i][0]][actual_pos[i][1]] = 0

            self.mostrarMatVali()
            # retorna false cuando la pieza no está dentro de la plantilla
            return False

    def IsComplete(self):
        if len(self.ma_vali) == 0:
            return False
        for i in range(len(self.ma_vali)):
            if 0 in self.ma_vali[i]:
                return False
        return True

    def mostrarMatVali(self):
        for i in self.ma_vali:
            print(i, end="\n")
        print()

    def borrarRastro(self):
        for i in self.Figuras:
            i.setMatPos([])
            i.setIniPos()

    def getMat(self):
        return self.ma_vali

    def getTabla_pc(self):
        return self.tabla_pc

    def getPiezas(self):
        return self.piezas

    # DibujarPlantilla1
    def DrawTemplate1(self, surface, x, y):
        brick_size = (50, 50)
        card = RetriveCard(1)
        mat = card.GetMatrix()

        # Draw graphix
        y = self.y
        for row in mat:
            x = self.x
            for column in row:
                if 0 == column:
                    pygame.draw.rect(surface, self.color, [(x, y), brick_size], 5)
                x += 50
            y += 50

        # Matrix
        if len(self.ma_vali) == 0:
            # NOTE: replace 1 with -1 ?
            self.ma_vali = mat
        pass

    # 3 Fichas
    def DibujarPlantilla1(self, surface, x, y):
        self.color = (randint(1, 150), randint(1, 150), randint(1, 150))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)], 5)
        # Fila
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)

        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                               00001
                                               10001
                                               10000
                                               11001
                                               """
        )
        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, 0, 0, -1], [-1, 0, 0, 0, -1], [-1, 0, 0, 0, 0], [-1, -1, 0, 0, -1]]

    # 3 FICHAS
    def DibujarPlantilla2(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)], 5)
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 250), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                                         001
                                                         000
                                                         000
                                                         000
                                                         110
                                                         110
                                                         """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [-1, -1, 0], [-1, -1, 0]]

    # 4 FICHAS
    def DibujarPlantilla3(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)], 5)
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 250), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                                      1000
                                                      0000
                                                      0000
                                                      1000
                                                      1001
                                                      1001
                                                      """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, -1], [-1, 0, 0, -1]]

    # 4 FICHAS
    def DibujarPlantilla4(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 150), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                                    10011
                                                    00011
                                                    00001
                                                    10000
                                                    """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [
                [-1, 0, 0, -1, -1],
                [0, 0, 0, -1, -1],
                [0, 0, 0, 0, -1],
                [
                    -1,
                    0,
                    0,
                    0,
                    0,
                ],
            ]

    # 4 FICHAS
    def DibujarPlantilla5(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 200), (50, 50)], 5)
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                               1100
                                               1100
                                               0000
                                               0000
                                               0000
                                               1011
                                               """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, -1, 0, 0], [-1, -1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [-1, 0, -1, -1]]

    # 4 FICHAS
    def DibujarPlantilla6(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 200), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                               1100
                                               1100
                                               0000
                                               0000
                                               1000
                                               """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, -1, 0, 0], [-1, -1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0]]

    # 4 FICHAS
    def DibujarPlantilla7(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        # Fila 5
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 200), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 200), (50, 50)], 5)
        # Fila 6
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 250), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 250), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                               1001
                                               1000
                                               1000
                                               0000
                                               0011
                                               0011
                                               """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[-1, 0, 0, -1], [-1, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, -1, -1], [0, 0, -1, -1]]

    # 4 FICHAS
    def DibujarPlantilla8(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                               0000
                                               0000
                                               1000
                                               1000
                                               """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]]

    # 4 FICHAS
    def DibujarPlantilla9(self, surface, x, y):
        self.color = (randint(1, 180), randint(1, 180), randint(1, 180))
        self.x = x
        self.y = y

        # DIBUJAR TABLERO DE JUGADOR COMPUTADORA
        # Fila 1
        pygame.draw.rect(surface, self.color, [(self.x, self.y), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y), (50, 50)], 5)
        # Fila 2
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 50), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 50), (50, 50)], 5)
        # Fila 3
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 100), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 100), (50, 50)], 5)
        # Fila 4
        pygame.draw.rect(surface, self.color, [(self.x, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 50, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 100, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 150, self.y + 150), (50, 50)], 5)
        pygame.draw.rect(surface, self.color, [(self.x + 200, self.y + 150), (50, 50)], 5)
        self.tabla_pc = backtracking_ubongo.gen_matrix(
            """
                                               00111
                                               00000
                                               00000
                                               00000
                                               """
        )

        if len(self.ma_vali) == 0:
            self.ma_vali = [[0, 0, -1, -1, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def getFiguras(self):
        return self.Figuras

    def vaciarMaVali(self):
        self.ma_vali = []

    def cargarFiguras(self, surface, cara, nplantilla):
        if nplantilla == 1:
            if cara == 0:
                self.Figuras[3].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                220
                                                                020
                                                                022
                                                                """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                           33
                                                           33
                                                           03
                                                           """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                        4
                                                        4
                                                        4
                                                        """
                    ),
                ]
            elif cara == 1:
                self.Figuras[9].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                20
                                                                22
                                                                02
                                                                """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                           33
                                                           33
                                                           03
                                                           """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                        44
                                                        04
                                                        04
                                                        """
                    ),
                ]
            elif cara == 2:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  03
                                                                  03
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                04
                                                44
                                                04
                                                """
                    ),
                ]
            elif cara == 3:
                self.Figuras[1].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       20
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                ]
            elif cara == 4:
                self.Figuras[6].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                         02
                                                         22
                                                         22
                                                         """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                    3333
                                                    """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                 04
                                                 44
                                                 40
                                                 """
                    ),
                ]
            elif cara == 5:
                self.Figuras[9].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[3].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                               20
                                                               22
                                                               02
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                          33
                                                          33
                                                          """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                       440
                                                       040
                                                       044
                                                       """
                    ),
                ]

        if nplantilla == 2:
            if cara == 0:
                self.Figuras[6].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                ]
            elif cara == 1:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               04
                                                               04
                                                               44
                                                               """
                    ),
                ]
            elif cara == 2:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                ]
            elif cara == 3:
                self.Figuras[7].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                              02
                                                                              22
                                                                              02
                                                                              02
                                                                              """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                         30
                                                                         33
                                                                         03
                                                                         """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      44
                                                                      04
                                                                      04
                                                                      """
                    ),
                ]
            elif cara == 4:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                ]
            elif cara == 5:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               4
                                                               4
                                                               4
                                                               4
                                                               """
                    ),
                ]
        if nplantilla == 3:
            if cara == 0:
                self.Figuras[9].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       20
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               4
                                                               4
                                                               4
                                                               4
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               05
                                                               55
                                                               05
                                                               05
                                                               """
                    ),
                ]
            elif cara == 1:
                self.Figuras[3].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       220
                                                                       020
                                                                       022
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               5
                                                               5
                                                               5
                                                               5
                                                               """
                    ),
                ]
            elif cara == 2:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               05
                                                               55
                                                               05
                                                               05
                                                               """
                    ),
                ]
            elif cara == 3:
                self.Figuras[7].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               55
                                                               55
                                                               05
                                                               """
                    ),
                ]
            elif cara == 4:
                self.Figuras[4].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               04
                                                               04
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               50
                                                               55
                                                               05
                                                               """
                    ),
                ]
            elif cara == 5:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               5
                                                               5
                                                               5
                                                               5
                                                               """
                    ),
                ]

        if nplantilla == 4:
            if cara == 0:
                self.Figuras[4].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                ]
            elif cara == 1:
                self.Figuras[9].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                          20
                                                                          22
                                                                          02
                                                                          """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                     33
                                                                     03
                                                                     03
                                                                     """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  04
                                                                  44
                                                                  04
                                                                  04
                                                                  """
                    ),
                ]
            elif cara == 2:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               40
                                                               44
                                                               """
                    ),
                ]
            elif cara == 3:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               04
                                                               04
                                                               44
                                                               """
                    ),
                ]
            elif cara == 4:
                self.Figuras[9].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       20
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                ]
            elif cara == 5:
                self.Figuras[11].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                          22
                                                                          22
                                                                          """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                     03
                                                                     33
                                                                     03
                                                                     03
                                                                     """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  44
                                                                  04
                                                                  04
                                                                  """
                    ),
                ]

        if nplantilla == 5:
            if cara == 0:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      5
                                                                      5
                                                                      5
                                                                      """
                    ),
                ]
            elif cara == 1:
                self.Figuras[11].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               40
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      55
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 2:
                self.Figuras[4].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[3].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               440
                                                               040
                                                               044
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      5
                                                                      5
                                                                      5
                                                                      5
                                                                      """
                    ),
                ]
            elif cara == 3:
                self.Figuras[11].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      05
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 4:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.Figuras[3].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               440
                                                               040
                                                               044
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                       05
                                                       05
                                                       05
                                                       55
                                                       """
                    ),
                ]
            elif cara == 5:
                self.Figuras[6].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      05
                                                                      05
                                                                      """
                    ),
                ]

        if nplantilla == 6:
            if cara == 0:
                self.Figuras[0].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      5
                                                                      5
                                                                      5
                                                                      5
                                                                      """
                    ),
                ]
            elif cara == 1:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      5
                                                                      5
                                                                      """
                    ),
                ]
            elif cara == 2:
                self.Figuras[4].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      05
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 3:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      5
                                                                      5
                                                                      """
                    ),
                ]
            elif cara == 4:
                self.Figuras[8].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      55
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 5:
                self.Figuras[9].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       20
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               4
                                                               4
                                                               4
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      05
                                                                      05
                                                                      """
                    ),
                ]

        if nplantilla == 7:
            if cara == 0:
                self.Figuras[1].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       20
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               05
                                                               05
                                                               05
                                                               55
                                                               """
                    ),
                ]
            elif cara == 1:
                self.Figuras[6].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               40
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               55
                                                               55
                                                               05
                                                               """
                    ),
                ]
            elif cara == 2:
                self.Figuras[0].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[3].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               550
                                                               050
                                                               055
                                                               """
                    ),
                ]
            elif cara == 3:
                self.Figuras[7].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               50
                                                               55
                                                               """
                    ),
                ]
            elif cara == 4:
                self.Figuras[5].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               40
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               55
                                                               05
                                                               05
                                                               """
                    ),
                ]
            elif cara == 5:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               04
                                                               04
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               55
                                                               55
                                                               05
                                                               """
                    ),
                ]

        if nplantilla == 8:
            if cara == 0:
                self.Figuras[8].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               5
                                                               5
                                                               """
                    ),
                ]
            elif cara == 1:
                self.Figuras[5].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               5
                                                               5
                                                               5
                                                               """
                    ),
                ]
            elif cara == 2:
                self.Figuras[2].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       02
                                                                       02
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               4
                                                               4
                                                               4
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               05
                                                               55
                                                               05
                                                               """
                    ),
                ]
            elif cara == 3:
                self.Figuras[7].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.Figuras[8].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  33
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               4
                                                               4
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               5
                                                               5
                                                               5
                                                               """
                    ),
                ]
            elif cara == 4:
                self.Figuras[6].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                2
                                                                2
                                                                2
                                                                2
                                                                """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                           3
                                                           3
                                                           """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                        44
                                                        04
                                                        04
                                                        """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                        55
                                                        55
                                                        """
                    ),
                ]
            elif cara == 5:
                self.Figuras[8].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[0].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               40
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               5
                                                               5
                                                               """
                    ),
                ]

        if nplantilla == 9:
            if cara == 0:
                self.Figuras[10].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.Figuras[3].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               440
                                                               040
                                                               044
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      55
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 1:
                self.Figuras[6].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       2
                                                                       2
                                                                       2
                                                                       2
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               04
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      05
                                                                      55
                                                                      05
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 2:
                self.Figuras[4].cargarImg(surface)
                self.Figuras[7].cargarImg(surface)
                self.Figuras[9].cargarImg(surface)
                self.Figuras[11].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  03
                                                                  33
                                                                  03
                                                                  03
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               40
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      55
                                                                      """
                    ),
                ]
            elif cara == 3:
                self.Figuras[1].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      20
                                                                      22
                                                                      """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                 33
                                                                 33
                                                                 03
                                                                 """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                              44
                                                              44
                                                              """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                     05
                                                                     05
                                                                     05
                                                                     55
                                                                     """
                    ),
                ]
            elif cara == 4:
                self.Figuras[7].cargarImg(surface)
                self.Figuras[1].cargarImg(surface)
                self.Figuras[2].cargarImg(surface)
                self.Figuras[4].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       02
                                                                       22
                                                                       02
                                                                       02
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  30
                                                                  33
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               04
                                                               04
                                                               04
                                                               44
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      05
                                                                      55
                                                                      05
                                                                      """
                    ),
                ]
            elif cara == 5:
                self.Figuras[11].cargarImg(surface)
                self.Figuras[6].cargarImg(surface)
                self.Figuras[5].cargarImg(surface)
                self.Figuras[10].cargarImg(surface)
                self.piezas = [
                    backtracking_ubongo.gen_matrix(
                        """
                                                                       22
                                                                       22
                                                                       """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                  3
                                                                  3
                                                                  3
                                                                  3
                                                                  """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                               44
                                                               44
                                                               04
                                                               """
                    ),
                    backtracking_ubongo.gen_matrix(
                        """
                                                                      55
                                                                      05
                                                                      05
                                                                      """
                    ),
                ]
