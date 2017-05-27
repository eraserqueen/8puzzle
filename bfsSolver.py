from Fringe import Fringe
from board import Board
from node import Node
from solver import Solver


class BfsFringe(Fringe):
    def add(self, item):
        if isinstance(item, Board):
            self.queue.append(Node(item))
        elif isinstance(item, Node):
            self.queue.append(item)
        return self

    def add_all(self, nodes):
        self.queue.extend(nodes)
        return self


class BfsSolver(Solver):
    strategy = 'BFS'

    def __init__(self, starting_board):
        self.fringe = BfsFringe().add(starting_board)
        super().__init__()
