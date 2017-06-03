from bfsSolver import BfsSolver
from dfsSolver import DfsSolver
import resource


class Driver:
    def __init__(self, strategy, starting_state):
        tiles = [int(i) for i in starting_state.replace(',', '')]
        starting_board = tiles
        if strategy == 'bfs':
            self.solver = BfsSolver(starting_board)
        if strategy == 'dfs':
            self.solver = DfsSolver(starting_board)

    def run(self):
        result = self.solver.run()
        usage = resource.getrusage(0)
        result.max_ram_usage = usage[2] / 8 / 1024 / 1024
        result.running_time = usage[0]
        return result


if __name__ == '__main__':
    import sys

    output = Driver(sys.argv[1], sys.argv[2]).run()
    f = open('output.txt', 'w')
    f.write(str(output))
    f.close()
    print(str(output))
