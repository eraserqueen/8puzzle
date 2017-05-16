from src.main.board import Board


class Node:
    def __init__(self, board, path=None):
        assert isinstance(board, Board)
        self.board = board
        if path is None:
            self.path = []
        else:
            self.path = path

    def __eq__(self, other):
        return self.board == other.board and self.depth == other.depth

    def __str__(self):
        if self.depth == 0:
            return "root"
        return str(self.depth) + "".join([s[0].upper() for s in self.path])

    @property
    def depth(self): return len(self.path)
