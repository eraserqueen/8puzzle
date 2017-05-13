class Result:
    def __init__(self):
        self.path_to_goal = []
        self.cost_of_path = 0
        self.nodes_expanded = 0
        self.search_depth = 0
        self.max_search_depth = 0
        self.running_time = 0
        self.max_ram_usage = 0

    @property
    def stringified(self):
        return f"""path_to_goal: {self.path_to_goal}
cost_of_path: {self.cost_of_path}
nodes_expanded: {self.nodes_expanded}
search_depth: {self.search_depth}
max_search_depth: {self.max_search_depth}
running_time: {self.running_time}
max_ram_usage: {self.max_ram_usage}"""