from checkers.models.checkerboard import Checkerboard
from checkers.models.checker import Checker


class TestCheckBoard:

    def test_checker_board_view(self):
        checker_board = Checkerboard()

        correct_checker_board = ("-0-0-0-0\n"
                                 + "0-0-0-0-\n"
                                 + "-0-0-0-0\n"
                                 + "0-0-0-0-\n"
                                 + "-0-0-0-0\n"
                                 + "0-0-0-0-\n"
                                 + "-0-0-0-0\n"
                                 + "0-0-0-0-\n")
        print("Correct")
        print(correct_checker_board)
        print("Mine")
        print(str(checker_board))
        assert correct_checker_board == str(checker_board)

    def test_checker_board_view_with_checkers(self):
        checker_board = Checkerboard()
        red_checker = Checker(0, 0, "black")
        black_checker = Checker(1, 1, "red")
        checker_board.add_checker(red_checker)
        checker_board.add_checker(black_checker)

        correct_checker_board = (
      "-0-0-0-0\n"
                                 + "0-0-0-0-\n"
                                 + "-0-0-0-0\n"
                                 + "0-0-0-0-\n"
                                 + "-0-0-0-0\n"
                                 + "0-0-0-0-\n"
                                 + "-r-0-0-0\n"
                                 + "b-0-0-0-\n"
        )
        print(correct_checker_board)
        assert correct_checker_board == str(checker_board)
