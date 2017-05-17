from collections import deque

from src.main.node import Node
from src.main.result import Result


class BfsSolver:
    strategy = 'BFS'

    def __init__(self, starting_board):
        self.fringe = deque([Node(starting_board)])
        self.visited = []
        self.result = Result()

    def run(self):
        while len(self.fringe) > 0:
            self.check_next_node()
        return self.result

    def check_next_node(self):
        current_node = self.fringe.popleft()

        if self.result.max_search_depth < current_node.depth:
            self.result.max_search_depth = current_node.depth

        if current_node.board.is_solved:
            self.fringe.clear()
            self.result.path_to_goal = current_node.path
            self.result.nodes_expanded = len(self.visited)
            self.result.search_depth = current_node.depth
            return

        try:
            self.visited.index(current_node)
        except ValueError:
            self.visited.append(current_node)
            next_nodes = [Node(state[1], current_node.path[:] + [state[0]])
                          for state in current_node.board.next_states]
            self.fringe.extend(next_nodes)
