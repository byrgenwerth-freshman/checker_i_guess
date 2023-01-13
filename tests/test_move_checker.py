from models.checker import Checker
from handlers.move_handler import MoveHandler


class TestMoveChecker:

    def test_move_checker(self):
        checker = Checker(0, 0)
        move_handler = MoveHandler()

        assert move_handler.move(checker, 'r')

        assert 1 == checker.x
        assert 1 == checker.y

    def test_move_checker_fails_off_board(self):
        checker = Checker(0, 0)
        move_handler = MoveHandler()

        assert not move_handler.move(checker, 'l')

        assert 0 == checker.x
        assert 0 == checker.y
