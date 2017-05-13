from board import Board

class Driver:
    def __init__(self, strategy, starting_state):
        self.strategy = strategy
        tiles = [int(i) for i in starting_state.replace(',', '')]
        self.board = Board(tiles)

    def run(self):
        return "Solved puzzle with " + self.strategy.upper()


if __name__ == '__main__':
    import sys
    Driver(sys.argv[1], sys.argv[2])
