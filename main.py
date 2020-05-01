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
    xs = 1200
    ys = 800

    # Superfice que se toma
    surface = screen.set_mode([xs, ys])

    pygame.display.flip()

    # Reloj
    reloj = pygame.time.Clock()

    #Se crea la lista de Escenarios
    Esc = Escenarios()
    
    # Se crea la lista con todas las figuras
    Figuras = []
    Figuras.append(CFigura(randint(0,1000),randint(0,700),1,"Fichas/Ficha1.png"))
    Figuras.append(CFigura(randint(0,1000),randint(0,700),2,"Fichas/Ficha2.png"))
    Figuras.append(CFigura(randint(0,1000),randint(0,700),3,"Fichas/Ficha3.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),4,"Fichas/Ficha4.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),5,"Fichas/Ficha5.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),6,"Fichas/Ficha6.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),7,"Fichas/Ficha7.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),8,"Fichas/Ficha8.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),9,"Fichas/Ficha9.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),10,"Fichas/Ficha10.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),11,"Fichas/Ficha11.png"))
    #Figuras.append(CFigura(randint(0,1000),randint(0,700),12,"Fichas/Ficha12.png"))
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
                    aux.rotarImg(0)
                    
                #si la tecla es "a" rota es sentido anti-horario
                elif event.key == pygame.K_a and aux != 0:
                    aux.rotarImg(0)
                    
            #Si se apreta un boton del mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #si el boton es izquierdo
                if event.button == pygame.BUTTON_LEFT:
                    pixel = list(surface.get_at((x, y)))
                    #se busca la figura que coincida con la pos del cursor
                    for i in range(len(Figuras)):
                        if pixel == list(Figuras[i].getCol()):
                            #se activa el movimiento
                            activate = True
                            aux = Figuras[i]
                            
                #si el boton es derecho
                elif event.button == pygame.BUTTON_RIGHT:
                    #se cancela el movimiento
                    activate = False
                    aux = 0
                    
        #FPS fijados en 20
        reloj.tick(20)
        x,y = pygame.mouse.get_pos()
        #Cambio de pos de la figura seleccionada
        if activate:
            aux.setPos(x, y)
        
        surface.fill((100, 0, 255))
        # Se cargan todas las figuras
        for i in range(len(Figuras)):
            Figuras[i].cargarImg(surface)

        Esc.DibujarPlantilla1(surface)

        screen.update()


main()
