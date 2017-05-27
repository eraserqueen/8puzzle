from collections import deque

from node import Node
from result import Result


class Solver:
    strategy = ''

    def __init__(self, starting_board):
        self.fringe = deque([Node(starting_board)])
        self.visited = set()

    def run(self):
        while len(self.fringe) > 0:
            self.check_next_node()

        return Result().compute(self.visited)

    def check_next_node(self):
        current_node = self.fringe.popleft()
        self.add_to_visited(current_node)

        if current_node.board.is_solved:
            self.fringe.clear()
            return

        if current_node.is_final:
            return

        next_nodes = []
        for next_node in current_node.next_states:
            if self.should_add_to_fringe(next_node):
                next_nodes.append(next_node)

        if len(next_nodes) > 0:
            self.add_to_fringe(next_nodes)

    def add_to_visited(self, current_node):
        self.visited.add(current_node)

    def should_add_to_fringe(self, next_node):
        if next_node in self.visited:
            return False
        try:
            self.fringe.index(next_node)
            return False
        except ValueError:
            return True
