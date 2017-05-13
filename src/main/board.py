class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        print("initialised board with:" + str(self.tiles))

    def is_solved(self):
        return self.tiles == [0, 1, 2, 3, 4, 5, 6, 7, 8]
