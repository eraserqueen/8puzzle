from collections import deque

from node import Node
from result import Result


class Solver:
    strategy = ''

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
        self.visited.append(current_node)

        if current_node.board.is_solved:
            self.fringe.clear()
            self.result.path_to_goal = self.find_path(current_node)
            self.result.nodes_expanded = len(self.visited)-1
            self.result.search_depth = current_node.depth
            return

        if current_node.is_final:
            return

        next_nodes = []
        for state in current_node.next_states:
            next_node = Node(state[1], state[0], current_node.depth+1)
            try:
                self.visited.index(next_node)
                continue
            except ValueError:
                pass
            try:
                self.fringe.index(next_node)
                continue
            except ValueError:
                pass
            next_nodes.append(next_node)
            if self.result.max_search_depth < next_node.depth:
                self.result.max_search_depth = next_node.depth

        if len(next_nodes)> 0:
            self.add_to_fringe(next_nodes)

    def find_path(self, node):
        path = []
        while node.origin is not None:
            path.append(node.origin)
            getattr(node.board, node.reverse_move)()
            node = self.visited[self.visited.index(node)]
        path.reverse()
        return [m[0].upper()+m[1:] for m in path]
