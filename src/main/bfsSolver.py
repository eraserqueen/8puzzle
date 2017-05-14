import copy

from src.main.result import Result


class BfsSolver:
    strategy = 'BFS'

    def __init__(self, starting_board):
        self.state = starting_board

    def run(self):
        return Result()

    def next_states(self, board):
        states = []
        for m in board.valid_moves:
            next_state = copy.deepcopy(board)
            getattr(next_state, m)()
            states.append(next_state)
        return states
