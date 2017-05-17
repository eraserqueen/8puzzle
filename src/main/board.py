import copy

class Board:
    solved_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, tiles=None):
        if tiles is None:
            self.tiles = self.solved_tiles
        else:
            self.tiles = tiles

    def __str__(self):
        return str(self.tiles)

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

    @property
    def valid_moves(self):
        moves = ["up", "down", "left", "right"]
        if self.empty_slot < 3:
            moves.remove("up")
        if self.empty_slot > 5:
            moves.remove("down")
        if self.empty_slot % 3 == 0:
            moves.remove("left")
        if self.empty_slot % 3 == 2:
            moves.remove("right")
        return moves

    @property
    def next_states(self):
        return [(move, getattr(copy.copy(self), move)()) for move in self.valid_moves]

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
