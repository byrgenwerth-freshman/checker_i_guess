from checkers.models.checker import Checker
from checkers.models.checkerboard import Checkerboard


class MoveHandler:

    checkerboard = None

    def __init__(self, checkboard: Checkerboard):
        self.checkboard = checkboard

    def move(self, checker: Checker, direction: str) -> bool:
        if direction == 'r':
            temp_x = checker.x + 1
            temp_y = checker.y + 1
            if not self.valid_position(temp_x, temp_y):
                return False
            if self.jump_check(checker, temp_x, temp_y, direction):
                temp_x += 1
                temp_y += 1

        if direction == 'l':
            temp_x = checker.x - 1
            temp_y = checker.y + 1
            if not self.valid_position(temp_x, temp_y):
                return False
            if self.jump_check(checker, temp_x, temp_y, direction):
                temp_x -= 1
                temp_y += 1

        self.checkboard.checkers[(checker.x, checker.y)] = None
        checker.x = temp_x
        checker.y = temp_y
        self.checkboard.checkers[(checker.x, checker.y)] = checker

        return True

    # pylint: disable=invalid-name
    def valid_position(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x > 8 or y > 8:
            return False
        return True

    def jump_check(self, checker: Checker, x: int, y: int,
                   direction: str) -> bool:
        if (x, y) in self.checkboard.checkers:
            jumped_checker = self.checkboard.checkers[(x, y)]
            if jumped_checker.color != checker.color:
                if direction == 'l':
                    empty_x = x - 1
                    empty_y = x + 1

                if direction == 'r':
                    empty_x = x + 1
                    empty_y = x + 1
                if (self.valid_position(empty_x, empty_y)
                        and not self.checkboard.checkers.get(
                            (empty_x, empty_y))):
                    self.checkboard.checkers[(x, y)] = None
                    return True
        return False
