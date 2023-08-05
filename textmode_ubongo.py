import CardTemplateReader
import Piece
from Fichas import readTextFile


def main2():
    pieces = readTextFile()
    print(f"Number of pieces: {len(pieces)}")

    card_reader = CardTemplateReader.CardTemplateReader()
    cards = card_reader.ReadFile()
    print(cards)
    for i in range(2):
        num = i + 1
        print(f"Card {num}")
        card_reader.PrintBoard(num)

    for key in pieces.keys():
        pp = Piece.Piece(pieces[key]["shape"])
        pp.produce_variants()
        pp.output(name=str(key))


if "__main__" == __name__:
    main2()
