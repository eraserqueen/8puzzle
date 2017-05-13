class Board:
    def __init__(self, tiles):
        self.tiles = tiles

    def is_solved(self):
        return self.tiles == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    @property
    def empty_slot(self): return self.tiles.index(0)

    def swap(self, swapped_slot):
        self.tiles[self.empty_slot] = self.tiles[swapped_slot]
        self.tiles[swapped_slot] = 0

    def down(self):
        self.swap(self.empty_slot + 3)

    def up(self):
        self.swap(self.empty_slot - 3)

    def left(self):
        self.swap(self.empty_slot - 1)

    def right(self):
        self.swap(self.empty_slot + 1)

