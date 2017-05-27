import unittest

from board import Board
from node import Node
from result import Result, find_node, find_max_depth, find_path


class TestResult(unittest.TestCase):
    def test_init(self):
        result = Result()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.cost_of_path)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)
        self.assertEqual(0, result.max_search_depth)
        self.assertEqual(0, result.running_time)
        self.assertEqual(0, result.max_ram_usage)

    def test_str(self):
        result = Result()
        expected = 'path_to_goal: []\n' + \
                   'cost_of_path: 0\n' + \
                   'nodes_expanded: 0\n' + \
                   'search_depth: 0\n' + \
                   'max_search_depth: 0\n' + \
                   'running_time: 0\n' + \
                   'max_ram_usage: 0'
        self.assertEqual(expected, str(result))

    def test_find_max_depth(self):
        node_set = {Node(Board(), None, 1),
                    Node(Board([1, 2, 3, 4, 5, 6, 7, 8, 0]), None, 2),
                    Node(Board([2, 3, 4, 5, 6, 7, 8, 0, 1]), None, 3),
                    Node(Board([3, 4, 5, 6, 7, 8, 0, 1, 2]), None, 4)}
        self.assertEqual(4, find_max_depth(node_set))

    def test_find_path(self):
        goal_node = Node(Board([0, 1, 2, 3, 4, 5, 6, 7, 8]), "left", 3)
        visited_set = {goal_node,
                       Node(Board([1, 0, 2, 3, 4, 5, 6, 7, 8]), "left", 2),
                       Node(Board([1, 2, 0, 3, 4, 5, 6, 7, 8]), "up", 1),
                       Node(Board([1, 2, 5, 3, 4, 0, 6, 7, 8]), None, 0),
                       }

        self.assertEqual(["Up", "Left", "Left"], find_path(goal_node, visited_set))

    def test_find_node_returns_node_when_match_is_found(self):
        previous = Node(Board(), None, 0)
        current = Node(Board().right(), "right", 1)
        visited_set = {previous}
        self.assertEqual(previous, find_node(current.prev_state, visited_set))

    def test_find_node_returns_none_when_no_match_is_found(self):
        other = Node(Board().down(), "up", 0)
        current = Node(Board().right(), "right", 1)
        visited_set = {other}
        self.assertEqual(None, find_node(current, visited_set))


if __name__ == '__main__':
    unittest.main()
