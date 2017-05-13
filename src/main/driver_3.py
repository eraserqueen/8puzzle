from board import Board
from result import Result


class Driver:
    def __init__(self, strategy, starting_state):
        self.strategy = strategy
        tiles = [int(i) for i in starting_state.replace(',', '')]
        self.board = Board(tiles)
        self.result = Result()

    def run(self):
        print(f"running with {self.strategy.upper()}")
        output = self.result.stringified
        print(output)
        return output


if __name__ == '__main__':
    import sys
    Driver(sys.argv[1], sys.argv[2]).run()
