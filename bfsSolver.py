from Fringe import Fringe
from node import Node
from solver import Solver


class BfsFringe(Fringe):
    def add(self, node):
        self.queue.append(node)
        super().add(node)
        return self

    def add_all(self, nodes):
        self.queue.extend(nodes)
        super().add_all(nodes)
        return self


class BfsSolver(Solver):
    strategy = 'BFS'

    def __init__(self, starting_board):
        self.fringe = BfsFringe().add(Node(starting_board))
        super().__init__()
