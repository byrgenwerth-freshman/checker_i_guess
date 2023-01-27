class Checker:

    color = None
    x = None
    y = None
    king = False

    # pylint: disable=invalid-name
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
