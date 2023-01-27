from checkers.models.checker import Checker


class Checkerboard:

    checkers = None

    def __init__(self):
        self.checkers = {}

    def add_checker(self, checker: Checker):
        if self.checkers.get((checker.x, checker.y)):
            print("Checker already exists")
        else:
            self.checkers[(checker.x, checker.y)] = checker

    def __repr__(self):

        board = [
            "0-0-0-0-",
            "-0-0-0-0",
            "0-0-0-0-",
            "-0-0-0-0",
            "0-0-0-0-",
            "-0-0-0-0",
            "0-0-0-0-",
            "-0-0-0-0",
        ]
        for loc in self.checkers:
            checker = self.checkers.get(loc)
            if checker:
                temp = list(board[loc[0]])

                temp[loc[1]] = self.get_ui_checker(checker.color)
                board[loc[0]] = "".join(temp)
        board.reverse()
        print_board = ""
        for line in board:
            print_board += f"""{line}\n"""
        return print_board

    def get_ui_checker(self, color: str):
        if color == 'red':
            return 'r'
        if color == 'black':
            return 'b'
