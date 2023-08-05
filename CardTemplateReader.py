import re


class CardTemplateReader:
    def __init__(self):
        self.cards = {}
        self.board_mode = False

    def ReadFile(self):
        def add_card(card, board, problems):
            if "card" not in card:
                print("No card")
                return
            id = card["card"]
            card["board"] = board
            card["problems"] = problems
            self.cards[id] = card
            print(card)
            self.board_mode = False

        filename = "cards.txt"
        re_card = re.compile(r"Card:")
        re_board = re.compile(r"Board:")
        re_problem = re.compile(r"Problem:")
        re_pieces = re.compile(r"Pieces:")

        card = {}
        board = []
        problems = {}
        problem = 99
        with open(filename, "rt") as fp:
            lineno = 0
            for line1 in fp.readlines():
                lineno += 1
                line2 = line1.strip()
                if 0 == len(line2):
                    self.board_mode = False
                    # print(f"Empty: {lineno}")

                    if False and board:
                        add_card(card, board, problems)
                        card = {}
                        board = []
                        problems = {}

                elif re_card.match(line2):
                    if board:
                        self.board_mode = False
                        add_card(card, board, problems)
                        card = {}
                        board = []
                        problems = {}
                        problem = 99
                    temp = line2.split(":")
                    second = temp[1].strip()
                    card = {"card": int(second)}
                    # print(f"card={second}")

                elif re_problem.match(line2):
                    temp = line2.split(":")
                    second = temp[1].strip()
                    problem = int(second)
                    # print(f"  problem={problem}")

                elif re_pieces.match(line2):
                    temp = line2.split(":")
                    second = temp[1].strip()
                    temp2 = second.split(",")
                    pice_numbers = []
                    for x in temp2:
                        pice_numbers.append(int(x.strip()))
                    problems[problem] = pice_numbers
                    # print(f"    problems[ {problem} ] = {pice_numbers}")

                elif re_board.match(line2):
                    self.board_mode = True

                elif self.board_mode:
                    board.append([int(c) for c in line2])

            if card:
                add_card(card, board, problems)
        return self.cards

    def PrintBoard(self, num):
        card = self.cards[num]
        board = card["board"]
        for row in board:
            s = "|"
            for col in row:
                if 0 == col:
                    s += "."
                elif 1 == col:
                    s += "X"
            s += "|"
            print(s)
        count = 2 + len(board[0])
        print("+" * count)
