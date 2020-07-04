import sys
import pygame
from pygame.locals import *
import pygame_menu
import numpy as np
import backtracking_ubongo as bu
from FichasyTableros import *
from DadosyGemas import *
from Jugador import *

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
# inicializar Pygame
pygame.init()

# establecer el título de la ventana
pygame.display.set_caption('Ubongo!!!')

# Tamaño de la pantalla para menu
xs = 1200
ys = 800

#LETRAS
menufont = pygame.font.Font(None,48)

def drawTablero(dimensiones, pantalla):
    pygame.draw.rect(pantalla, (0, 0, 0), [0, 0, dimensiones[0], dimensiones[1]])
    pygame.draw.rect(pantalla, (240, 128, 0), [12 * (an), 0, dimensiones[0] - (an), dimensiones[1]])
    pygame.draw.rect(pantalla, (128, 55, 0), [16 * (an), 0, dimensiones[0] - (an), dimensiones[1]])

    for y in range(0, 7):
        pygame.draw.line(pantalla, (92, 38, 7), (0, y * (la)), (dimensiones[0] - 1, y * (la)), 2)
    for x in range(1, 13):
        pygame.draw.line(pantalla, (92, 38, 7), (x * (an), 0), (x * (an), dimensiones[1] - 1), 2)

# Parametros para dibujar el tablero
dimensiones = [1000, 300]
an = dimensiones[0] / 18
la = dimensiones[1] / 6

#Menu e instrucciones
def menuOpciones():
    reloj = pygame.time.Clock()
    running = True
    while running:
        display = pygame.display.set_mode((xs, ys))
        display.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 400, 50)
        button_2 = pygame.Rect(150, 200, 400, 50)
        button_3 = pygame.Rect(250, 300, 400, 50)

        pygame.draw.rect(display, (255, 0, 0), button_1)
        pygame.draw.rect(display, (0, 255, 0), button_2)
        pygame.draw.rect(display, (0, 0, 255), button_3)
        imagen1 = pygame.image.load("dibujo1.png")
        display.blit(imagen1, (460, 200))
        imagen2 = pygame.image.load("dibujo2.png")
        display.blit(imagen2, (760, 100))

        start = menufont.render('Comenzar Juego', True, (0, 255, 0))
        instrucciones = menufont.render('Instrucciones', True, (0, 0, 255))
        quit = menufont.render('Salir', True, (255, 255, 255))

        display.blit(start, (90, 112))
        display.blit(instrucciones, (225, 210))
        display.blit(quit, (400, 310))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                return True
        if button_2.collidepoint((mx, my)):
            if click:
                return False
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        reloj.tick(60)

def instrucciones():
    reloj = pygame.time.Clock()
    running = True
    while running:

        display = pygame.display.set_mode((xs, ys))
        display.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 50, 150, 50)
        button_2 = pygame.Rect(50, 100, 150, 50)

        imagen1 = pygame.image.load("instrucciones.png")
        display.blit(imagen1, (-40, 0))
        pygame.draw.rect(display, (0, 255, 0), button_1)
        pygame.draw.rect(display, (255, 0, 0), button_2)
        empezar = menufont.render('Empezar', True, (0, 0, 255))
        volver = menufont.render('Salir', True, (0, 0, 255))
        display.blit(empezar, (55, 60))
        display.blit(volver, (78, 110))

        if button_1.collidepoint((mx, my)):
            if click:
                return True
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        reloj.tick(60)

def cambiarPlantillasPiezas(Esc,Esc2,surface,Dado,origenPlantillaEnemigo):
    Esc2.vaciarMaVali()
    NumeroPlantilla_Jugador = randint(1,9)
    NumeroPlantilla_PC = randint(1,9)
    DefinirPlantillaPC(NumeroPlantilla_PC, Esc, surface, origenPlantillaEnemigo)
    DefinirPlantillaJugador(NumeroPlantilla_Jugador,Esc2, surface, 100)
    Esc2.borrarRastro()
    tabla = Esc.getTabla_pc()
    Dado.tirar(surface)
    caraDado = Dado.getRes()-1
    Esc.cargarFiguras(surface,caraDado,NumeroPlantilla_PC)
    piezas = Esc.getPiezas()
    print(piezas)
    # solucion será de las mismas dimensiones de la tabla
    solucion = [[0 for j in range(len(tabla[i]))] for i in range(len(tabla))]
    # mandamos las piezas, la tabla y la tabla que traerá la solución
    bu.resolucion(piezas, tabla, solucion)
    contSol = [0,0,0,0]
    ocur = [0,0,0,0]

    for i in range(len(solucion)):
        for j in range(2,6):
           ocur[j-2] +=  solucion[i].count(j)

    #captura tiempo
    global tiempoFinal
    tiempoFinal = pygame.time.get_ticks()
    
    return NumeroPlantilla_Jugador, NumeroPlantilla_PC, tabla, piezas, solucion,ocur,contSol


def main():

    screen = pygame.display

    # Superfice que se toma
    surface = screen.set_mode([xs, ys])
    #tiempoLimite = None
    pygame.display.flip()

    # Datos del tablero
    Dado = dado()
    gemas = []
    gemas = gema.inicializarGemas(gemas)

    #Booleano que permite jugar con las piezas
    armarPuzzle = False

    # Creacion de las fichas de los jugadores
    players = []
    players = jugador.creacionDeFichasDeLosJugadores(players)

    # creación y disposición de las gemas en el tablero, color al azar
    for y in range(0, 6):
        for x in range(0, 12):
            gemas[y][x] = gema(x * an, y * la, random.randint(1, 6))

    # Se crea la lista de Escenarios
    # Esc -> enemigo
    # Esc2 -> jugador
    Esc = Plantilla(900, 400)
    Esc2 = Plantilla(500, 400)
    # Variables controladoras
    # X y Y sirven para obtener la posicion del raton
    x = 0
    y = 0
    
    origenPlantillaJugador = 500
    origenPlantillaEnemigo = 900

    ##### CONTROL DE PARTIDA #######
    # Numero de partidas restantes al inicio
    partidasRestantes = 9
    partidasGanadas = 0
    partidasGanadas_PC = 0


    # Bool que activa o desactiva el movimiento
    activate = False

    # aux -> Tomará los valores de la Figura seleccionada
    aux = 0

    #Plantillas aleatorias que se le asigna al jugador y a la máquina
    NumeroPlantilla_Jugador = randint(1,9)
    NumeroPlantilla_PC = randint(1,9)
    DefinirPlantillaPC(NumeroPlantilla_PC, Esc, surface, origenPlantillaEnemigo)
    Dado.tirar(surface)
    DefinirPlantillaJugador(NumeroPlantilla_Jugador,Esc2,surface,origenPlantillaJugador)

    # SOLUCION CON BACTRACKING -> Jugador Computadora
    tabla = Esc.getTabla_pc()
    Esc.cargarFiguras(surface,randint(0,5),NumeroPlantilla_PC)
    piezas = Esc.getPiezas()
    print(len(piezas))
    # solucion será de las mismas dimensiones de la tabla
    solucion = [[0 for j in range(len(tabla[i]))] for i in range(len(tabla))]
    # mandamos las piezas, la tabla y la tabla que traerá la solución
    bu.resolucion(piezas, tabla, solucion)
    # después que el algoritmo cambió a la variable solución ya la tenemos para usarla
    print("solucion:")
    print(np.matrix(solucion))
    print()
    contSol = [0,0,0,0]
    ocur = [0,0,0,0]

    for i in range(len(solucion)):
        for j in range(2,6):
           ocur[j-2] +=  solucion[i].count(j)
    print(ocur)

    # Booleano que controla el while principal
    running = True

    # Reloj
    current_time = 0
    reloj = pygame.time.Clock()
    # FPS fijados en 20
    reloj.tick(20)
    contadorPiezasPuestas = 0

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
                if event.key == pygame.K_a and aux != 0:
                    aux.rotarImg(0)

                # Si la tecla es "q" la imgaen se voltea
                if event.key == pygame.K_q and aux != 0:
                    aux.voltearImg()

                # teclas tablero
                if event.key == K_e and players[0].capacidadRecoleccion > 0:
                    players[0].ganargemas(gemas)
                    players[0].capacidadRecoleccion -= 1
                if event.key == K_r and players[1].capacidadRecoleccion > 0:
                    players[1].ganargemas(gemas)
                    players[1].capacidadRecoleccion -= 1
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
                if event.key == K_x and partidasRestantes > 0:
                    if(armarPuzzle == False):
                        armarPuzzle = True
                        tiempo_inicio = pygame.time.get_ticks()

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

        # Computadora recolecta fichas por si sola

        def movimientoPC():
            direccion = random.randint(0, 1)

            if direccion == 0 and players[1].movidas > 0 and players[1].y - la >= 0:
                players[1].y = players[1].y - la
                players[1].movidas = players[1].movidas - 1
            if direccion == 1 and players[1].movidas > 0 and players[1].y + la <= la * 6:
                players[1].y = players[1].y + la
                players[1].movidas = players[1].movidas - 1
            recoleccionGemasPC()

        def recoleccionGemasPC():
            if players[1].capacidadRecoleccion > 0:
                players[1].ganargemas(gemas)
                players[1].capacidadRecoleccion -= 1

        print("movidas PC: {}".format(players[1].movidas))
        print("movidas PC: {}".format(players[1].capacidadRecoleccion))


        x, y = pygame.mouse.get_pos()

        # Cambio de pos de la figura seleccionada
        if activate:
            aux.setPos(x, y)

        surface.fill((211, 111, 111))

        # Plantilla enemiga
        origenY = 400
        width = 50
        height = 50
        color1 = (255, 0, 0)
        color2 = (0, 255, 0)
        color3 = (0, 0, 255)
        color4 = (127, 0, 255)

        #Se cargan las plantillas
        if(armarPuzzle):
        # Puzzle Jugador
            if (Esc2.IsComplete() == True):
                armarPuzzle = False
                print("ganaste")
                partidasGanadas += 1
                players[0].movidas += 2
                players[0].capacidadRecoleccion += 2
                players[1].movidas += 1
                players[1].capacidadRecoleccion += 1
                movimientoPC()
                movimientoPC()
                contadorPiezasPuestas = 0
                NumeroPlantilla_Jugador, NumeroPlantilla_PC, tabla, piezas, solucion,ocur,contSol = cambiarPlantillasPiezas(Esc,Esc2,surface,Dado,origenPlantillaEnemigo)
                # Si se gana la partida actual, aparece este mensaje
                partidasRestantes = partidasRestantes - 1
                ganar1 = menufont.render('Ganaste esta partida. Quedan {} partidas.'.format(partidasRestantes),
                                             True, (0, 255, 0))
                surface.blit(ganar1, (100, 633))
            else: 
                DefinirPlantillaPC(NumeroPlantilla_PC, Esc, surface,origenPlantillaEnemigo)
                DefinirPlantillaJugador(NumeroPlantilla_Jugador,Esc2, surface,origenPlantillaJugador)

                current_time = pygame.time.get_ticks()

                # Backtracking enemigo
                for yy in range(len(solucion)):
                    for xx in range(len(solucion[yy])):
                        if solucion[yy][xx] == 2 and current_time >= (tiempoLimite * 0.25) + tiempo_inicio:
                            if(contSol[0] < ocur[0]):
                                contSol[0]+=1
                            pygame.draw.rect(surface, color1,
                                             [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                        if solucion[yy][xx] == 3 and current_time >= (tiempoLimite * 0.5) + tiempo_inicio:
                            if(contSol[1] < ocur[1]):
                                contSol[1]+=1
                            pygame.draw.rect(surface, color2,
                                             [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                        if solucion[yy][xx] == 4 and current_time >= (tiempoLimite * 0.75) + tiempo_inicio:
                            if(contSol[2] < ocur[2]):
                                contSol[2]+=1
                            pygame.draw.rect(surface, color3,
                                             [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])
                        if solucion[yy][xx] == 5 and current_time >= tiempoLimite + tiempo_inicio:
                            if(contSol[3] < ocur[3]):
                                contSol[3]+=1
                            pygame.draw.rect(surface, color4, [(origenPlantillaEnemigo + (xx * 50), origenY + (yy * 50)), (width, height)])

        # para tablero
        drawTablero(dimensiones, surface)

        # Para el tablero

        for j in range(6):
            for i in range(12):
                if gemas[j][i] != 0:
                    gemas[j][i].dibujargema(surface)

        for j in range(len(players)):
            players[j].dibujarjugador(surface)

            #desactivar. Si esta activada se inhabilita el movimiento
           # if players[j].movidas <= 0:
                #players[j].mueve = False

        Dado.dibujarDado(Dado.res, surface)

        if(armarPuzzle):
            # Se cargan todas las figuras
            Esc2.cargarFiguras(surface, Dado.getRes()-1, NumeroPlantilla_Jugador)

        #Separador
        pygame.draw.line(surface, (0, 0, 0), (800, dimensiones[1]), (800, 900), 20)

        # Display nombres jugador y computadora
        displayNombreJugador = menufont.render('{}'.format(nombreJugador), True, (0, 0, 0))
        surface.blit(displayNombreJugador, (20, 720))
        displayPartidasGanadas = menufont.render('Partidas ganadas: {}'.format(partidasGanadas), True, (0, 255, 0))
        surface.blit(displayPartidasGanadas, (20, 750))
        displayNombreComputadora = menufont.render('HAL 9000', True, (0, 0, 0))
        surface.blit(displayNombreComputadora, (1100, 720))
        displayPartidasGanadas_PC = menufont.render('Partidas ganadas: {}'.format(partidasGanadas_PC), True, (120, 0, 0))
        surface.blit(displayPartidasGanadas_PC, (1020, 750))

        # Display partidas restantes
        displayPartidasRestantes = menufont.render('Partidas restantes: {}'.format(partidasRestantes), True, (0, 0, 0))
        surface.blit(displayPartidasRestantes, (600, 720))

        # Mostrar al ganador cuando acaban 9 partidas
        if partidasRestantes == 0:
            ganadorFont = pygame.font.SysFont("comicsansms",80)
            displayGanador = ganadorFont.render('{}, ganaste!!!'.format(nombreJugador), True,(0, 180, 0))
            surface.blit(displayGanador, (200, 450))
            displayTiempoJugado = menufont.render("Jugaste {} milisegundos!".format(tiempoFinal - tiempoInicioDePartida), True,(0, 180, 0))
            surface.blit(displayTiempoJugado, (200, 650))

        screen.update()

        if(armarPuzzle):
            if(contSol[0] == ocur[0] and contSol[1] == ocur[1] and contSol[2] == ocur[2] and contSol[3] == ocur[3]):
                print("perdiste")
                partidasGanadas_PC += 1
                players[0].movidas = 1
                players[0].capacidadRecoleccion = 1
                players[1].movidas = 2
                players[1].capacidadRecoleccion = 2
                movimientoPC()
                movimientoPC()
                armarPuzzle = False
                NumeroPlantilla_Jugador, NumeroPlantilla_PC, tabla, piezas, solucion,ocur,contSol = cambiarPlantillasPiezas(Esc,Esc2,surface,Dado,origenPlantillaEnemigo)
                perder1 = menufont.render('Perdiste esta partida. Quedan {} partidas.'.format(partidasRestantes), True, (0, 0, 0))
                surface.blit(perder1, (400, 550))
                partidasRestantes = partidasRestantes - 1
                contadorPiezasPuestas = 0
                Dado.tirar(surface)


screen = pygame.display
surface = screen.set_mode([xs, ys])

#Inicializar variables de partida
global tiempoLimite
tiempoLimite = 30000
global nombreJugador
nombreJugador = 'player'

menuOpciones()

if menuOpciones()==False:
    instrucciones()

def start_the_game():
    global tiempoInicioDePartida
    tiempoInicioDePartida = pygame.time.get_ticks()
    menu.disable()

def set_difficulty(value, difficulty):
    global current_time
    current_time = 0
    global tiempoLimite
    tiempoLimite = difficulty

def check_name(value, nombre):
    global nombreJugador
    nombreJugador = value
    #print(nombreJugador)

menu = pygame_menu.Menu(400, 400, 'Ubongo',
                        theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add_text_input('Nombre :', nombre='', onchange=check_name)
menu.add_selector('Dificultad :', [('Dificil', 30000), ('Medio', 60000), ('Facil', 90000)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

main()
