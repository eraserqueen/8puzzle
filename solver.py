from result import Result


class Solver:
    def __init__(self):
        self.visited = set()

    def run(self):
        while self.fringe.has_nodes():
            self.check_next_node()
        return Result().compute(self.visited)

    def check_next_node(self):
        node = self.fringe.get_next_node()
        self.add_to_visited(node)

        if node.board.is_solved:
            self.fringe.clear()
            return

        if node.is_final:
            return

        next_nodes = []
        for next_node in node.next_states:
            if self.should_add_to_fringe(next_node):
                next_nodes.append(next_node)

        if len(next_nodes) > 0:
            self.fringe.add_all(next_nodes)

    def add_to_visited(self, current_node):
        self.visited.add(current_node)

    def should_add_to_fringe(self, next_node):
        return next_node not in self.visited and next_node not in self.fringe
