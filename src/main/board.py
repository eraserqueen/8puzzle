import copy


class Board:
    def __init__(self, tiles):
        self.tiles = tiles

    def __str__(self):
        return str(self.tiles)

    def __eq__(self, other):
        if self is None:
            return other is None
        elif other is None:
            return self is None
        else:
            return self.tiles == other.tiles

    @property
    def is_solved(self):
        return self.tiles == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    @property
    def empty_slot(self): return self.tiles.index(0)

    @property
    def valid_moves(self):
        moves = ["up", "down", "left", "right"]
        if self.empty_slot < 3:
            moves.remove("up")
        if self.empty_slot > 5:
            moves.remove("down")
        if self.empty_slot%3 == 0:
            moves.remove("left")
        if self.empty_slot%3 == 2:
            moves.remove("right")
        return moves

    @property
    def next_states(self):
        states = [
            copy.copy(self).up(),
            copy.copy(self).down(),
            copy.copy(self).left(),
            copy.copy(self).right(),
        ]
        return states

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
