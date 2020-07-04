
def gen_matrix(string):
    return [[int(x) for x in line.strip()] for line in string.strip().split('\n')]


def is_valid(pos, board):
    # Revisa si cada tupla de posicion (x,y) está en el tablero
    x, y = pos;
    if x < 0 or y < 0:
        return False
    if x > len(board[0]) or y > len(board):
        return False
    return True


def insert_piece(piece, pos, board, remove=False):
    corner_x, corner_y = pos

    for dx in range(len(piece[0])):
        for dy in range(len(piece)):
            x, y = corner_x + dx, corner_y + dy;
            assert (is_valid((x, y), board))

            if piece[dy][dx] != 0:
                board[y][x] = piece[dy][dx] if not remove else 0


def can_insert(piece, pos, board):
    corner_x, corner_y = pos
    for dx in range(len(piece[0])):
        for dy in range(len(piece)):
            x, y = corner_x + dx, corner_y + dy
            assert (is_valid((x, y), board))

            if piece[dy][dx] != 0 and board[y][x] != 0:
                return False
    return True


def permutations(piece):
    piece = tuple(tuple(row) for row in piece)
    rotations = {
        piece,
        tuple(reversed(piece))
    }
    for _ in range(3):  # Add the 3 other rotations
        piece = tuple(tuple(reversed(row)) for row in zip(*piece))
        flipped = tuple(reversed(piece))  # Included the flipped version
        rotations.add(piece)
        rotations.add(flipped)
    return rotations


def print_2d(array):
    for row in array:
        print(' '.join(map(str, (x if x != 1 else ' ' for x in row))))

    print()


def solve(pieces, board, solu):
    # Caso Base: No hay mas fichas que añadir
    if len(pieces) == 0:
        for i in range(len(board)):
            for j in range(len(board[i])):
                solu[i][j] = board[i][j]
        return
    # Siguiente pieza en ser añadida
    piece = pieces[0]

    # Intentar con cada orientación y coordenadas válidas
    for rotation in permutations(piece):
        for x in range(len(board[0]) - len(rotation[0]) + 1):
            for y in range(len(board) - len(rotation) + 1):
                if can_insert(rotation, (x, y), board):
                    # Si la coordenada es válida, insertar pieza
                    insert_piece(rotation, (x, y), board)
                    # Se intenta añadir las piezas adicionales
                    solve(pieces[1:], board, solu)
                    # Backtracking para intentar añadir en distintos lugares
                    insert_piece(rotation, (x, y), board, remove=True)


def resolucion(pieces, board, solu):
    solve(pieces, board, solu)
    return solu
