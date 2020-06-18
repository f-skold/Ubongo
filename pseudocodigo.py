
def isLegal(pieza, puzzle, posicion, rotacion):
    if puzzle.vacio(posicion, pieza.ancho, pieza.alto):
        return True
    else:
        if(rotacion):
            pieza.rotar()
            if isLegal(pieza, puzzle,posicion, rotacion-1):
                return True
        else: return False
    
def backtracking(posicion,puzzle):
    if cantidad_piezas < n:
        for pieza in range(len(lista_piezas)):
            if isLegal(pieza, puzzle, posicion, 6):
                puzzle.colocar(pieza)
                backtracking(piezas, puzzle, cantidad_piezas+1)
                puzzle.sacar(pieza)
    else:
        return puzzle