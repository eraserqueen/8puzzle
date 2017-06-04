from collections import deque


class Fringe:
    def __init__(self, items=None):
        if items is None:
            self.queue = deque()
            self.hashes = set()
            self.max_depth = 0
        else:
            self.queue = deque(items)
            self.hashes = set([hash(node) for node in items])
            self.max_depth = max(node.depth for node in items)

    def add(self, item):
        self.__add(item)

    def add_all(self, items):
        for item in items:
            self.__add(item)

    def __add(self, item):
        self.hashes.add(hash(item))
        if item.depth > self.max_depth:
            self.max_depth = item.depth

    def has_nodes(self):
        return len(self.hashes) > 0

    def get_next_node(self):
        node = self.queue.popleft()
        h = hash(node)
        self.hashes.remove(h)
        return node

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
