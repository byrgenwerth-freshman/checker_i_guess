from checkers.models.checker import Checker


class Checkerboard:

    checkers = {}

    def __init__(self):
        pass

    def add_checker(self, checker: Checker):
        if self.checkers.get((checker.x, checker.y)):
            print("Checker already exists")
        else:
            self.checkers[(checker.x, checker.y)] = checker

    def __repr__(self):
        return """
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️️️
        """
