from src.main.board import Board


class Node:
    def __init__(self, board, depth=None, path=None):
        assert isinstance(board, Board)
        self.board = board
        if depth is None:
            self.depth = 0
        else:
            self.depth = depth
        if path is None:
            self.path = []
        else:
            self.path = path

    def __eq__(self, other):
        return self.board == other.board and self.depth == other.depth
