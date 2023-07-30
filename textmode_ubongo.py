import CardTemplateReader
from Fichas import readTextFile


def main2():
    pieces = readTextFile()
    print(f"Number of pieces: {len(pieces)}")

    card_reader = CardTemplateReader.CardTemplateReader()
    cards = card_reader.ReadFile()


if "__main__" == __name__:
    main2()
