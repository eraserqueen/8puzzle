from Moves import *


def swap(board, direction):
    empty_slot = board.index(0)
    swapped_slot = empty_slot + direction
    if not (0 <= swapped_slot < 9):
        return None
    else:
        new_board = board[:]
        new_board[empty_slot] = new_board[swapped_slot]
        new_board[swapped_slot] = 0
        return new_board


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
        return "({0}) {1} {2}".format(self.depth, "".join([str(i) for i in self.board]), self.origin)

    def __hash__(self):
        result = 0
        multiplier = 1
        for i in self.board:
            result += i*multiplier
            multiplier = multiplier*10
        return result

    @property
    def valid_moves(self):
        moves = [Moves.UP, Moves.DOWN, Moves.LEFT, Moves.RIGHT]
        if self.origin is not None:
            moves.remove(self.origin * -1)
        empty_slot = self.board.index(0)
        if empty_slot < 3:
            moves.remove(Moves.UP)
        if empty_slot > 5:
            moves.remove(Moves.DOWN)
        if empty_slot % 3 == 0:
            moves.remove(Moves.LEFT)
        if empty_slot % 3 == 2:
            moves.remove(Moves.RIGHT)
        return moves

    @property
    def next_states(self):
        return [Node(swap(self.board, direction), direction, self.depth + 1)
                for direction
                in self.valid_moves]

    @property
    def prev_board(self):
        if self.origin is None or self.depth == 0:
            return None
        return swap(self.board, self.origin * -1)
