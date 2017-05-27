import copy


class Node:
    def __init__(self, board, origin=None, depth=None):
        self.board = board
        self.origin = origin
        if depth is None:
            self.depth = 0
        else:
            self.depth = depth

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.board == other.board

    def __str__(self):
        return "({0}) {1} {2}".format(self.depth, str(self.board), self.origin)

    def __hash__(self):
        return int(self.board)

    @property
    def reverse_move(self):
        if self.origin is None:
            return None
        reverse_moves = {"up": "down", "down": "up", "left": "right", "right": 'left'}
        return reverse_moves[self.origin]

    @property
    def valid_moves(self):
        moves = ["up", "down", "left", "right"]
        if self.board.empty_slot < 3 or self.origin == "down":
            moves.remove("up")
        if self.board.empty_slot > 5 or self.origin == "up":
            moves.remove("down")
        if self.board.empty_slot % 3 == 0 or self.origin == "right":
            moves.remove("left")
        if self.board.empty_slot % 3 == 2 or self.origin == "left":
            moves.remove("right")
        return moves

    @property
    def is_final(self): return len(self.valid_moves) == 0

    @property
    def next_states(self):
        if self.is_final:
            return None
        return [(move, getattr(copy.copy(self.board), move)()) for move in self.valid_moves]