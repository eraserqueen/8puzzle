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

    @property
    def cost_of_path(self): return len(self.path_to_goal)
