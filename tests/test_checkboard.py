from checkers.models.checkerboard import Checkerboard


class TestCheckBoard:

    def test_checker_board_view(self):
        checker_board = Checkerboard()

        correct_checker_board = """
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️
        ⬜️⬛️⬜️⬛️⬜️⬛️️⬜️⬛️️️
        ️⬛️⬜️⬛️⬜️⬛️️⬜️⬛⬜️️️️️
        """
        assert correct_checker_board == str(checker_board)
