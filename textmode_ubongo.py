import CardTemplateReader
import Piece
from Fichas import readTextFile


def main2():
    pieces = readTextFile()
    print(f"Number of pieces: {len(pieces)}")

    card_reader = CardTemplateReader.CardTemplateReader()
    card_reader.ReadFile()
    for i in range(2):
        print(f"Card {i + 1}")
        card_reader.PrintBoard(i + 1)

    for key in pieces.keys():
        pp = Piece.Piece(pieces[key]["shape"])
        pp.produce_variants()
        pp.output(name=str(key))


if "__main__" == __name__:
    main2()
