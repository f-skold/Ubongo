import re


class CardTemplateReader:
    def __init__(self):
        self.cards = {}
        self.board_mode = False

    def ReadFile(self):
        def add_card(card, board):
            card["board"] = board
            id = card["card"]
            self.cards[id] = card
            print(card)
            self.board_mode = False

        filename = "cards.txt"
        re_card = re.compile(r"Card:")
        re_board = re.compile(r"Board:")

        card = {}
        board = []

        with open(filename, "rt") as fp:
            for line1 in fp.readlines():
                line2 = line1.strip()
                if 0 == len(line2):
                    if board:
                        add_card(card, board)
                        card = {}
                        board = []
                elif re_card.match(line2):
                    temp = line2.split(":")
                    second = temp[1].strip()
                    card = {"card": int(second)}

                elif re_board.match(line2):
                    self.board_mode = True
                elif self.board_mode:
                    board.append([int(c) for c in line2])

            if card:
                add_card(card, board)
        return self.cards
