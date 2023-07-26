from Fichas import readTextFile


def main2():
    pieces = readTextFile()
    print(f"Number of pieces: {len(pieces)}")


if "__main__" == __name__:
    main2()
