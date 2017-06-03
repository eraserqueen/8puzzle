from collections import deque


class Fringe:
    def __init__(self, items=None):
        if items is None:
            self.queue = deque()
            self.hashes = set()
        else:
            self.queue = deque(items)
            self.hashes = set([hash(node) for node in items])

    def add(self, item):
        self.hashes.add(hash(item))

    def add_all(self, items):
        for item in items:
            self.hashes.add(hash(item))

    def clear(self):
        self.queue.clear()

    def has_nodes(self):
        return len(self.queue) > 0

    def get_next_node(self):
        return self.queue.popleft()

    def __contains__(self, item):
        if item is None:
            return False
        return hash(item) in self.hashes

    def __eq__(self, other):
        if isinstance(other, Fringe):
            return self.queue == other.queue
        if isinstance(other, list):
            return list(self.queue) == other
        return False
