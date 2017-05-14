import copy
from collections import deque

from src.main.board import Board
from src.main.node import Node
from src.main.result import Result


class BfsSolver:
    strategy = 'BFS'

    def __init__(self, starting_board):
        assert isinstance(starting_board, Board)
        self.fringe = deque([Node(starting_board)])
        self.visited = []

    def run(self):
        while len(self.fringe) > 0:
            self.check_next_node()
        return Result()

    def check_next_node(self):
        current_node = self.fringe.popleft()
        if current_node.board.is_solved:
            self.fringe.clear()
            return
        try:
            self.visited.index(current_node)
        except ValueError:
            self.visited.append(current_node)
            next_nodes = [Node(board, current_node.depth + 1, current_node.path.append(move))
                          for (move, board) in current_node.board.next_states]
            self.fringe.extend(next_nodes)
