from checkers.models.checker import Checker
from checkers.models.checkerboard import Checkerboard
from checkers.handlers.move_handler import MoveHandler


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

    def test_red_checker_jumps_black_checker(self):
        checker_board = Checkerboard()
        red_checker = Checker(0, 0, "red")
        black_checker = Checker(1, 1, "black")
        checker_board.add_checker(red_checker)
        checker_board.add_checker(black_checker)

        move_handler = MoveHandler(checker_board)

        assert move_handler.move(red_checker, 'r')

        assert 2 == red_checker.x
        assert 2 == red_checker.y

        

        assert None == checker_board.checkers[(1, 1)]

        assert red_checker == checker_board.checkers[(2, 2)]
