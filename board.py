import copy


class Board:
    solved_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, tiles=None):
        if tiles is None:
            self.tiles = self.solved_tiles
        else:
            self.tiles = tiles

    def __str__(self):
        return "".join(str(t) for t in self.tiles)

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.tiles == other.tiles

    @property
    def is_solved(self):
        return self.tiles == self.solved_tiles

    @property
    def empty_slot(self):
        return self.tiles.index(0)

    def swap(self, swapped_slot):
        if not (0 <= swapped_slot < 9):
            return None
        else:
            tiles = copy.copy(self.tiles)
            tiles[tiles.index(0)] = tiles[swapped_slot]
            tiles[swapped_slot] = 0
            self.tiles = tiles
            return self

    def up(self):
        return self.swap(self.empty_slot - 3)

    def down(self):
        return self.swap(self.empty_slot + 3)

    def left(self):
        return self.swap(self.empty_slot - 1)

    def right(self):
        return self.swap(self.empty_slot + 1)
