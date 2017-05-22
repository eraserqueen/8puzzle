from solver import Solver


class BfsSolver(Solver):
    strategy = 'BFS'

    def add_to_fringe(self, next_nodes):
        self.fringe.extend(next_nodes)
