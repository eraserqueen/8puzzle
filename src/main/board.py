class Board:
    def __init__(self, tiles):
        self.state = tiles
        print("initialised board with:" + str(self.state))

    def is_solved(self):
        return self.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]
