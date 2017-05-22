from solver import Solver


class DfsSolver(Solver):
    strategy = 'DFS'

    def add_to_fringe(self, next_nodes):
        self.fringe.extendleft(next_nodes)
