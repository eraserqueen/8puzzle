from math import floor

from Fringe import Fringe
from node import Node
from solver import Solver


def distance_to_goal(board):
    distance = 0
    for i in range(9):
        if i == board[i]:
            continue
        row_distance = abs(floor(board[i] / 3) - floor(i / 3))
        col_distance = abs(floor(board[i] % 3) - floor(i % 3))
        distance += row_distance + col_distance
    return distance


class AstNode(Node):
    def __init__(self, board, origin=None, depth=None):
        super().__init__(board, origin, depth)
        self.cost = distance_to_goal(board) + self.depth


class AstFringe(Fringe):
    def add(self, node):
        i = 0
        while i < len(self.queue) and node.cost > self.queue[i].cost:
            i += 1
        self.insert(i, node)
        super().add(node)
        return self

    def insert(self, i, node):
        # use deque.insert >= python 3.5
        self.queue.rotate(-1*i)
        self.queue.appendleft(node)
        self.queue.rotate(i)

    def add_all(self, nodes):
        for n in nodes:
            self.add(n)
        return self


class AstSolver(Solver):
    strategy = 'AST'

    def __init__(self, starting_board):
        self.fringe = AstFringe().add(AstNode(starting_board))
        super().__init__()
