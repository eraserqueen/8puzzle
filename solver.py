import copy
from collections import deque
from node import Node
from result import Result


class Solver:
    strategy = ''

    def __init__(self, starting_board):
        self.fringe = deque([Node(starting_board)])
        self.visited = set()
        self.result = Result()

    def run(self):
        while len(self.fringe) > 0:
            self.check_next_node()
        return self.result

    def check_next_node(self):
        current_node = self.fringe.popleft()
        self.add_to_visited(current_node)

        if current_node.board.is_solved:
            self.result.path_to_goal = self.find_path(current_node)
            self.result.nodes_expanded = len(self.visited) - 1
            self.result.search_depth = current_node.depth
            return

        if current_node.is_final:
            return

        next_nodes = []
        for state in current_node.next_states:
            next_node = Node(state[1], state[0], current_node.depth + 1)
            if self.should_add_to_fringe(next_node):
                next_nodes.append(next_node)
                if self.result.max_search_depth < next_node.depth:
                    self.result.max_search_depth = next_node.depth

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

    def find_path(self, node):
        path = []
        while node.origin is not None:
            path.append(node.origin)
            next_node = copy.copy(node)
            getattr(next_node, next_node.reverse_move)()
            if next_node not in self.visited:
                return None
            for n in self.visited:
                if next_node == n:
                    node = n
                    continue
        path.reverse()
        return [m[0].upper() + m[1:] for m in path]
