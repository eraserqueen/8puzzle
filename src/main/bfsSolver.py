from src.main.result import Result

class BfsSolver:
    strategy = 'BFS'

    def __init__(self, startingState):
        print(f"running with {self.strategy}")
        self.state = startingState

    def run(self):
        return Result()