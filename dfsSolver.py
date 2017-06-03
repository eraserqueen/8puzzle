from Fringe import Fringe
from node import Node
from solver import Solver


class DfsFringe(Fringe):
    def add(self, item):
        self.queue.appendleft(item)
        return self

    def add_all(self, nodes):
        nodes.reverse()
        self.queue.extendleft(nodes)
        return self


class DfsSolver(Solver):
    strategy = 'DFS'

    def __init__(self, starting_board):
        self.fringe = DfsFringe().add(Node(starting_board))
        super().__init__()
