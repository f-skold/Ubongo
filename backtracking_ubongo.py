def gen_matrix(string):
    return [[int(x) for x in line.strip()] for line in string.strip().split("\n")]


def es_valido(pos, tabla):
    # Revisa si cada tupla de posicion (x,y) está en el tablero y no fuera
    x, y = pos
    if x < 0 or y < 0:
        return False
    if x > len(tabla[0]) or y > len(tabla):
        return False
    return True


def insertar_pieza(pieza, pos, tabla, remover=False):
    esquina_x, esquina_y = pos

    for dx in range(len(pieza[0])):
        for dy in range(len(pieza)):
            # asigna la pos inicial hasta la ultima pos de la pieza y la agrega en la tabla
            x, y = esquina_x + dx, esquina_y + dy
            # si retorna falso la función termina
            assert es_valido((x, y), tabla)

            if pieza[dy][dx] != 0:
                # esta linea sirve para remover o insertar dependiendo del valor de remover
                tabla[y][x] = pieza[dy][dx] if not remover else 0


def puede_insertar(pieza, pos, tabla):
    esquina_x, esquina_y = pos
    for dx in range(len(pieza[0])):
        for dy in range(len(pieza)):
            x, y = esquina_x + dx, esquina_y + dy
            assert es_valido((x, y), tabla)
            # si pretende insertarse en un espacio nulo retorn false
            if pieza[dy][dx] != 0 and tabla[y][x] != 0:
                return False
    return True


def rotaciones(pieza):
    pieza = tuple(tuple(fila) for fila in pieza)
    rotaciones = {
        pieza,
        # reverso vertical
        tuple(reversed(pieza)),
    }
    for _ in range(3):  # añade otra 3 rotaciones
        pieza = tuple(tuple(reversed(fila)) for fila in zip(*pieza))
        giro = tuple(reversed(pieza))  # Included the flipped version
        rotaciones.add(pieza)
        rotaciones.add(giro)
    return rotaciones


def resol(piezas, tabla, solu):
    # Caso Base: No hay mas fichas que añadir
    if len(piezas) == 0:
        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                solu[i][j] = tabla[i][j]
        return
    # Siguiente pieza en ser añadida
    pieza = piezas[0]

    # Intentar con cada orientación y coordenadas válidas
    for rotacion in rotaciones(pieza):
        for x in range(len(tabla[0]) - len(rotacion[0]) + 1):
            for y in range(len(tabla) - len(rotacion) + 1):
                if puede_insertar(rotacion, (x, y), tabla):
                    # Si la coordenada es válida, insertar pieza
                    insertar_pieza(rotacion, (x, y), tabla)
                    # Se intenta añadir las piezas adicionales
                    resol(piezas[1:], tabla, solu)
                    # Backtracking para intentar añadir en distintos lugares
                    insertar_pieza(rotacion, (x, y), tabla, remover=True)


def resolucion(piezas, tabla, solu):
    resol(piezas, tabla, solu)
    return solu
