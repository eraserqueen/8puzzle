class Result:
    def __init__(self):
        self.path_to_goal = []
        self.nodes_expanded = 0
        self.search_depth = 0
        self.max_search_depth = 0
        self.running_time = 0
        self.max_ram_usage = 0

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"""path_to_goal: {self.path_to_goal}
cost_of_path: {self.cost_of_path}
nodes_expanded: {self.nodes_expanded}
search_depth: {self.search_depth}
max_search_depth: {self.max_search_depth}
running_time: {self.running_time}
max_ram_usage: {self.max_ram_usage}"""

    @property
    def cost_of_path(self): return len(self.path_to_goal)