from src.main.board import Board
from src.main.bfsSolver import BfsSolver


class Driver:
    def __init__(self, strategy, starting_state):
        tiles = [int(i) for i in starting_state.replace(',', '')]
        starting_board = Board(tiles)
        if strategy == 'bfs':
            self.solver = BfsSolver(starting_board)

    def run(self):
        result = self.solver.run()
        return str(result)


if __name__ == '__main__':
    import sys
    Driver(sys.argv[1], sys.argv[2]).run()
