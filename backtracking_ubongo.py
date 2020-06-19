def gen_matrix(string):
    """Generates a matrix (2d array) from a multi-line string"""
    return [[int(x) for x in line.strip()] for line in string.strip().split('\n')]

def is_valid(pos, board):
    """Checks whether a given position tuple (x, y) is on the board"""
    x, y = pos;
    if x < 0 or y < 0:
        return False
    if x > len(board[0]) or y > len(board):
        return False
    return True

def insert_piece(piece, pos, board, remove=False):
    """
    Insert a given piece into the board, with pos as the top left corner.
    If the remove flag is set to true, it removes the given piece instead.
    """
    corner_x, corner_y = pos

    for dx in range(len(piece[0])):
        for dy in range(len(piece)):
            x, y = corner_x + dx, corner_y + dy;
            assert(is_valid((x, y), board))

            if piece[dy][dx] != 0:
                board[y][x] = piece[dy][dx] if not remove else 0

def can_insert(piece, pos, board):
    """
    Checks whether it is possible to insert the given piece at the given position.
    """
    corner_x, corner_y = pos
    for dx in range(len(piece[0])):
        for dy in range(len(piece)):
            x, y = corner_x + dx, corner_y + dy
            assert(is_valid((x, y), board))

            if piece[dy][dx] != 0 and board[y][x] != 0:
                return False
    return True

def permutations(piece):
    """
    Returns all the possible orientations of the given piece.
    If the piece is symmetrical, it only returns one of each identical version.
    """
    piece = tuple(tuple(row) for row in piece)
    rotations = {
        piece,
        tuple(reversed(piece))
    }
    for _ in range(3): # Add the 3 other rotations
        piece = tuple(tuple(reversed(row)) for row in zip(*piece))
        flipped = tuple(reversed(piece)) # Included the flipped version
        rotations.add(piece)
        rotations.add(flipped)
    return rotations

def print_2d(array):
    """
    Prints the given 2d array
    Tiles with a 1 (off the board) are not printed
    """
    for row in array:
        print(' '.join(map(str, (x if x != 1 else ' ' for x in row))))

    print()

def solve(pieces, board, solu):
    """Solves the ubongo puzzle"""
    # Base case: No more pieces to add.
    # Due to the way the puzzle is created, this means that the board is full.
    if len(pieces) == 0:
        print_2d(board)
        for i in range(len(board)):
                for j in range(len(board[i])):
                    solu[i][j] = board[i][j]
        return
    # This is the next piece we will add into the puzzle.
    piece = pieces[0]

    # Try every valid orientation, and starting location.
    for rotation in permutations(piece):
        for x in range(len(board[0]) - len(rotation[0]) + 1):
            for y in range(len(board) - len(rotation) + 1):
                if can_insert(rotation, (x, y), board):
                    # If the starting location is valid, insert the piece.
                    insert_piece(rotation, (x, y), board)
                    # Attempt to add the additional pieces. 
                    solve(pieces[1:], board,solu)
                    # Backtrack, so we can try different placements.
                    insert_piece(rotation, (x, y), board, remove=True)
                    
def resolucion(pieces,board, solu):
    solve(pieces,board, solu)
    return solu
    


"""
Format for describing puzzles:
All boards and pieces must be given as a rectangle. 
Locations which are not part of the board/piece should be "0"

0 --> empty space
1 --> unusable part of board
2-9 --> part of a piece

Each piece should use a different number, so they can be distinguished from each other.

Pieces and boards should be given in the smallest possible bounding rectangle.
I.e there should be no empty column/rows.
"""


"""for i, puzzle in enumerate(puzzles):
    print()
    print(f"Puzzle {i + 1} solutions:")
    print()
    board = puzzle['board']
    pieces = puzzle['pieces']
    solve(pieces, board)"""
    
    
