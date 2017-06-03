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
            self.depth = 1
        else:
            self.depth = depth

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.board == other.board

    def __str__(self):
        return "({0}) {1} {2}".format(self.depth, "".join([str(i) for i in self.board]), self.origin)

    def __hash__(self):
        return int("".join([str(i) for i in self.board]))

    @property
    def next_states(self):
        states = []
        for direction in [Moves.UP, Moves.DOWN, Moves.LEFT, Moves.RIGHT]:
            if self.origin is not None and direction == (-1 * self.origin):
                continue
            next_board = swap(self.board, direction)
            if next_board is None:
                continue
            states.append(Node(next_board, direction, self.depth + 1))
        return states

    @property
    def prev_board(self):
        if self.origin is None or self.depth == 0:
            return None
        return swap(self.board, self.origin * -1)
