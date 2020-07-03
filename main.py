import backtracking_ubongo as bu
from random import randint
from FichasyTableros import *
import numpy as np

def DefinirPlantillaJugador(NumeroPlantilla_Jugador, Esc2, surface, origenPlantillaJugador):
        #Dibujar Plantillas
        if(NumeroPlantilla_Jugador == 1):
            Esc2.DibujarPlantilla1(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 2:
            Esc2.DibujarPlantilla2(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 3: 
            Esc2.DibujarPlantilla3(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 4:
            Esc2.DibujarPlantilla4(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 5:
            Esc2.DibujarPlantilla5(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 6:
            Esc2.DibujarPlantilla6(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 7:
            Esc2.DibujarPlantilla7(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 8:
            Esc2.DibujarPlantilla8(surface, origenPlantillaJugador, 400)
        elif NumeroPlantilla_Jugador == 9:
            Esc2.DibujarPlantilla9(surface, origenPlantillaJugador, 400)

def DefinirPlantillaPC(NumeroPlantilla_PC,Esc, surface, origenPlantillaEnemigo):
        if(NumeroPlantilla_PC == 1):
            Esc.DibujarPlantilla1(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 2:
            Esc.DibujarPlantilla2(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 3:
            Esc.DibujarPlantilla3(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 4:
            Esc.DibujarPlantilla4(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 5:
            Esc.DibujarPlantilla5(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 6:
            Esc.DibujarPlantilla6(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 7:
            Esc.DibujarPlantilla7(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 8:
            Esc.DibujarPlantilla8(surface, origenPlantillaEnemigo, 400)
        elif NumeroPlantilla_PC == 9:
            Esc.DibujarPlantilla9(surface, origenPlantillaEnemigo, 400)

def main():

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

    # Se crea la lista de Escenarios
    # Esc -> enemigo
    # Esc2 -> jugador
    Esc = Plantilla(600, 400)
    # NO ME QUEDA CLARO COMO FUNCIONABA ESTO
    Esc2 = Plantilla(100, 400)

    # Variables controladoras
    # X y Y sirven para obtener la posicion del raton
    x = 0
    y = 0
    origenPlantillaJugador = 100
    origenPlantillaEnemigo = 400

    # Numero de partidas restantes al inicio
    partidasRestantes = 9

    # Booleano que controla el while principal
    running = True

    current_time = 0

    # Bool que activa o desactiva el movimiento
    activate = False

    # aux -> Tomará los valores de la Figura seleccionada
    aux = 0

    #Plantillas aleatorias que se le asigna al jugador y a la máquina
    NumeroPlantilla_Jugador = randint(1,9)
    NumeroPlantilla_PC = 1

    DefinirPlantillaPC(NumeroPlantilla_PC, Esc, surface, origenPlantillaEnemigo)

    tabla = Esc.getTabla_pc()
    Esc.cargarFiguras(surface,randint(0,5),NumeroPlantilla_PC)
    piezas = Esc.getPiezas()
    print(piezas)
    # solucion será de las mismas dimensiones de la tabla
    solucion = [[0 for j in range(len(tabla[i]))] for i in range(len(tabla))]
    # mandamos las piezas, la tabla y la tabla que traerá la solución
    bu.resolucion(piezas, tabla, solucion)
    # después que el algoritmo cambió a la variable solución ya la tenemos para usarla
    print("solucion:")
    print(np.matrix(solucion))
    print()


    # bucle infinito
    while running:

        # fuente para escribir texto:
        menufont = pygame.font.Font(None, 24)

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

                        #cambia a su posición inicial cuando tiene una posición invalida
                        if not Esc2.colocar(actualX, actualY, aux):
                          aux.setIniPos()  
                    aux = 0

        # FPS fijados en 20
        reloj.tick(20)
        x, y = pygame.mouse.get_pos()

        # Cambio de pos de la figura seleccionada
        if activate:
            aux.setPos(x, y)


        surface.fill((255, 139, 129))


        #Plantilla enemiga
        origenY = 400
        width = 50
        height = 50
        color1 = (255, 0, 0)
        color2 = (0, 255, 0)
        color3 = (0, 0, 255)
        color4 = (127, 0, 255)
        #Tiempo que demora la computadora en completar el puzzle
        tiempoLimite = 15000

        #Se cargan las plantillas
        DefinirPlantillaPC(NumeroPlantilla_PC, Esc, surface,origenPlantillaEnemigo) 
        DefinirPlantillaJugador(NumeroPlantilla_Jugador,Esc2, surface,origenPlantillaJugador)

        current_time = pygame.time.get_ticks()
        #Backtracking enemigo
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
                    if (Esc.DibujarPlantilla1 or Esc.DibujarPlantilla2 or Esc.DibujarPlantilla4):
                       partidasRestantes = partidasRestantes - 1
                       perder1 = menufont.render('Perdiste esta partida. Quedan {} partidas.'.format(partidasRestantes), True, (220, 0, 0))
                       surface.blit(perder1, (400, 550))

                #Si se supera el tiempo limite, computadora gana la partida
                if solucion[yy][xx] == 5 and current_time >= tiempoLimite:
                    partidasRestantes = partidasRestantes - 1
                    pygame.draw.rect(surface, color4,[(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                    perder1 = menufont.render('Perdiste esta partida. Quedan {} partidas.'.format(partidasRestantes), True, (220, 0, 0))
                    surface.blit(perder1, (400, 550))

        # Puzzle Jugador
        if (Esc2.IsComplete() == True):
            # Si se gana la partida actual, aparece este mensaje
            partidasRestantes = partidasRestantes - 1
            ganar1 = menufont.render('Ganaste esta partida. Quedan {} partidas.'.format(partidasRestantes), True,(220, 0, 0))
            surface.blit(ganar1, (100, 633))


        # Se cargan todas las figuras
        Esc2.cargarFiguras(surface, 0, NumeroPlantilla_Jugador)

        screen.update()


main()
