import copy
from collections import deque

from src.main.board import Board
from src.main.result import Result


def next_states(board):
    states = []
    for m in board.valid_moves:
        next_state = copy.deepcopy(board)
        getattr(next_state, m)()
        states.append(next_state)
    return states

class BfsSolver:
    strategy = 'BFS'

    def __init__(self, starting_board):
        assert isinstance(starting_board, Board)
        self.fringe = deque([starting_board])
        self.visited = []

    def run(self):
        while len(self.fringe) > 0:
            self.check_next_node()
        return Result()

    def check_next_node(self):
        current = self.fringe.popleft()
        if current.is_solved:
            self.fringe.clear()
            return
        try:
            self.visited.index(current)
        except ValueError:
            self.visited.append(current)
            self.fringe.extend(next_states(current))
