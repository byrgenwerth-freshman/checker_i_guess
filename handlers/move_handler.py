from models.checker import Checker


class MoveHandler:

    def move(self, checker: Checker, direction: str) -> bool:
        if direction == 'r':
            temp_x = checker.x + 1
            temp_y = checker.y + 1
            if not self.valid_position(temp_x, temp_y):
                return False

        if direction == 'l':
            temp_x = checker.x - 1
            temp_y = checker.y + 1
            if not self.valid_position(temp_x, temp_y):
                return False
        checker.x = temp_x
        checker.y = temp_y
        return True

    def valid_position(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x > 8 or y > 8:
            return False
        return True
