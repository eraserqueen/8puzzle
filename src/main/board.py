import copy


class Board:
    def __init__(self, tiles):
        self.tiles = tiles

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
        states = []
        for m in self.valid_moves:
            next_state = copy.deepcopy(self)
            getattr(next_state, m)()
            states.append(next_state)
        return states

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
