import backtracking_ubongo as bu
from FichasyTableros import *
import numpy as np


def main():

    # Booleano que controla el while principal
    running = True

    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption('Ubongo!!!')

    screen = pygame.display

    # Tamaño de la pantalla
    xs = 800
    ys = 800

    # Superfice que se toma
    surface = screen.set_mode([xs, ys])

    pygame.display.flip()

    # Reloj
    reloj = pygame.time.Clock()
    current_time = 0

    # Se crea la lista de Escenarios
    #Esc -> enemigo
    #Esc2 -> jugador
    Esc = Plantilla(600, 0)
    #NO ME QUEDA CLARO COMO FUNCIONABA ESTO
    Esc2 = Plantilla(100, 0)

    # Variables controladoras
    # X y Y sirven para obtener la posicion del raton
    x = 0
    y = 0
    # Bool que activa o desactiva el movimiento
    activate = False

    # aux -> Tomará los valores de la Figura seleccionada
    aux = 0

    # SOLUCION CON BACTRACKING DE LA PLANTILLA 1 CON SUS RESPECTIVAS PIEZAS
    #enemigo
    piezas = Esc.getPiezas()
    tabla = Esc.getTabla_pc()
    # solucion será de las mismas dimensiones de la tabla
    solucion = [[0 for j in range(len(tabla[i]))] for i in range(len(tabla))]
    # mandamos las piezas, la tabla y la tabla que traerá la solución
    bu.resolucion(piezas, tabla, solucion)
    # después que el algoritmo cambió a la variable solución ya la tenemos para usarla
    print("solucion:")
    print(np.matrix(solucion))
    print()

    piezas2 = Esc2.getPiezas()
    tabla2 = Esc2.getTabla_pc()
    print(np.matrix(tabla2))

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
                elif event.key == pygame.K_a and aux != 0:
                    aux.rotarImg(0)

                # Si la tecla es "q" la imgaen se voltea
                elif event.key == pygame.K_q and aux != 0:
                    aux.voltearImg()

            # Si se apreta un boton del mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # si el boton es izquierdo
                if event.button == pygame.BUTTON_LEFT:
                    pixel = list(surface.get_at((x, y)))
                    # se busca la figura que coincida con la pos del cursor
                    for i in range(len(Esc2.getFiguras())):
                        if pixel == list(Esc2.getFiguras()[i].getCol()):
                            # se activa el movimiento
                            activate = True
                            aux = Esc2.getFiguras()[i]

                # si el boton es derecho
                elif event.button == pygame.BUTTON_RIGHT:
                    # se cancela el movimiento
                    activate = False
                    # obtener la posicion del mouse
                    posmouse = pygame.mouse.get_pos()
                    if aux != 0:
                        aux.acomodarImg()
                        actualX, actualY = aux.getPos()
                        Esc2.colocar(actualX, actualY, aux)
                    aux = 0

        # FPS fijados en 20
        reloj.tick(20)
        x, y = pygame.mouse.get_pos()

        # Cambio de pos de la figura seleccionada
        if activate:
            aux.setPos(x, y)

        origenPlantillaJugador = 100
        origenPlantillaEnemigo = 400

        surface.fill((255, 139, 129))

        #Dibujar Plantillas
        Esc2.DibujarPlantilla1(surface, origenPlantillaJugador, 0)
        Esc.DibujarPlantilla6(surface, origenPlantillaEnemigo, 0)

        #Plantilla enemiga
        origenY = 250
        width = 50
        height = 50
        color1 = (255, 0, 0)
        color2 = (0, 255, 0)
        color3 = (0, 0, 255)
        color4 = (127, 0, 255)
        #Tiempo que demora la computadora en completar el puzzle
        tiempoLimite = 15000

        current_time = pygame.time.get_ticks()
        # print(current_time)

        for yy in range(len(solucion)):
            for xx in range(len(solucion[yy])):
                if solucion[yy][xx] == 2 and current_time >= tiempoLimite*0.25:
                    pygame.draw.rect(surface, color1,
                                     [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                if solucion[yy][xx] == 3 and current_time >= tiempoLimite*0.5:
                    pygame.draw.rect(surface, color2,
                                     [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                if solucion[yy][xx] == 4 and current_time >= tiempoLimite*0.75:
                    pygame.draw.rect(surface, color3,
                                     [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                # Si se supera el tiempo limite, computadora gana la partida
                if solucion[yy][xx] == 5 and current_time >= tiempoLimite:
                    pygame.draw.rect(surface, color4,
                                     [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                    menufont = pygame.font.Font(None, 24)
                    start = menufont.render('Perdiste esta partida. Quedan {i}.', True, (220, 0, 0))
                    surface.blit(start, (300, 550))

        # Se cargan todas las figuras
        Esc2.cargarFiguras(surface, 4, 0)

        # Imprimir Tiempo
        #print(current_time)

        # Pruebas
        #print(aux)

        screen.update()


main()
