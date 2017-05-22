from board import Board
from bfsSolver import BfsSolver
from dfsSolver import DfsSolver
import resource


class Driver:
    def __init__(self, strategy, starting_state):
        tiles = [int(i) for i in starting_state.replace(',', '')]
        starting_board = Board(tiles)
        if strategy == 'bfs':
            self.solver = BfsSolver(starting_board)
        if strategy == 'dfs':
            self.solver = DfsSolver(starting_board)

    def run(self):
        self.solver.run()
        usage = resource.getrusage(0)
        self.solver.result.max_ram_usage = usage[2] / 8 / 1024 / 1024
        self.solver.result.running_time = usage[0]
        return self.solver.result


if __name__ == '__main__':
    import sys

    result = Driver(sys.argv[1], sys.argv[2]).run()
    f = open('output.txt', 'w')
    f.write(str(result))
    f.close()
    print(str(result))
