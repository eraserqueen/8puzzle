from result import Result


class Solver:
    def __init__(self):
        self.visited = set()
        self.solution_found = False

    def run(self):
        while not self.solution_found and self.fringe.has_nodes():
            self.check_next_node()
        if not self.solution_found:
            return None
        return Result().compute(self.visited, self.fringe)

    def check_next_node(self):
        node = self.fringe.get_next_node()
        self.add_to_visited(node)

        if node.board == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            self.solution_found = True
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
