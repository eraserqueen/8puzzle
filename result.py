from node import Node


def find_max_depth(node_set):
    if len(node_set) == 0:
        return 0
    return max([node.depth for node in node_set])


def find_node(node, node_set):
    if node is None or node not in node_set:
        return None
    for n in node_set:
        if node == n:
            return n


def find_path(node, visited_set):
    working_set = set(visited_set)
    moves = {-3: "Up", 3: "Down", -1: "Left", 1: "Right"}
    path = []
    while node is not None and node.origin is not None:
        working_set.remove(node)
        path.append(node.origin)
        node = find_node(Node(node.prev_board), working_set)
    path.reverse()
    return [moves[m] for m in path]


class Result:
    def __init__(self):
        self.path_to_goal = []
        self.cost_of_path = 0
        self.nodes_expanded = 0
        self.search_depth = 0
        self.max_search_depth = 0
        self.running_time = 0
        self.max_ram_usage = 0

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return 'path_to_goal: {0}\n' \
               'cost_of_path: {1}\n' \
               'nodes_expanded: {2}\n' \
               'search_depth: {3}\n' \
               'max_search_depth: {4}\n' \
               'running_time: {5}\n' \
               'max_ram_usage: {6}' \
            .format(str(self.path_to_goal),
                    str(self.cost_of_path),
                    str(self.nodes_expanded),
                    str(self.search_depth),
                    str(self.max_search_depth),
                    str(self.running_time),
                    str(self.max_ram_usage))

    def compute(self, visited_set):
        from node import Node
        goal_node = find_node(Node([0, 1, 2, 3, 4, 5, 6, 7, 8]), visited_set)
        self.search_depth = goal_node.depth
        self.path_to_goal = find_path(goal_node, visited_set)
        self.cost_of_path = len(self.path_to_goal)
        self.nodes_expanded = len(visited_set) - 1
        # TODO: max_search_depth is off by one in bfs but not dfs, WTF??
        self.max_search_depth = find_max_depth(visited_set)
        return self
