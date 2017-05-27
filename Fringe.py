from collections import deque


class Fringe:
    def __init__(self, items=None):
        if items is None:
            self.queue = deque()
        else:
            self.queue = deque(items)

    def clear(self):
        self.queue.clear()

    def has_nodes(self):
        return len(self.queue) > 0

    def get_next_node(self):
        return self.queue.popleft()

    def __contains__(self, item):
        try:
            self.queue.index(item)
            return True
        except ValueError:
            return False

    def __eq__(self, other):
        if isinstance(other, Fringe):
            return self.queue == other.queue
        if isinstance(other, list):
            return list(self.queue) == other
        return False
