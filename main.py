
from FichasyTableros import *

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

    #Se crea la lista de Escenarios
    Esc = Plantilla(600,0)
    
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
                
            #Si se apreta una tecla
            elif event.type == pygame.KEYDOWN:
                #si la tecla es "d" rota en sentido horario
                if event.key == pygame.K_d and aux != 0:
                    aux.rotarImg(1)
                    
                #si la tecla es "a" rota es sentido anti-horario
                elif event.key == pygame.K_a and aux != 0:
                    aux.rotarImg(0)
                
                #Si la tecla es "q" la imgaen se voltea
                elif event.key == pygame.K_q and aux != 0:
                    aux.voltearImg()
                    
            #Si se apreta un boton del mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #si el boton es izquierdo
                if event.button == pygame.BUTTON_LEFT:
                    pixel = list(surface.get_at((x, y)))
                    #se busca la figura que coincida con la pos del cursor
                    for i in range(len(Esc.getFiguras())):
                        if pixel == list(Esc.getFiguras()[i].getCol()):
                            #se activa el movimiento
                            activate = True
                            aux = Esc.getFiguras()[i]
                            
                #si el boton es derecho
                elif event.button == pygame.BUTTON_RIGHT:
                    #se cancela el movimiento
                    activate = False
                    #obtener la posicion del mouse
                    posmouse = pygame.mouse.get_pos()
                    if aux != 0:
                        aux.acomodarImg()
                        actualX, actualY = aux.getPos()
                        Esc.colocar(actualX,actualY, aux)
                    aux = 0
                    
        #FPS fijados en 20
        reloj.tick(20)
        x,y = pygame.mouse.get_pos()
        
        #Cambio de pos de la figura seleccionada
        if activate:
            aux.setPos(x, y)
        
        origenPlantilla=400

        surface.fill((255,139,129))

        Esc.DibujarPlantilla1(surface,origenPlantilla,0)
        
        # Se cargan todas las figuras
        Esc.cargarFiguras(surface,4,0)
        
        screen.update()

main()
