import unittest

from Moves import *
from node import Node, swap
from result import Result, find_node, find_max_depth, find_path


class TestResult(unittest.TestCase):
    solved_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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
        node_set = {Node([0, 1, 2, 3, 4, 5, 6, 7, 8], None, 1),
                    Node([1, 2, 3, 4, 5, 6, 7, 8, 0], None, 2),
                    Node([2, 3, 4, 5, 6, 7, 8, 0, 1], None, 3),
                    Node([3, 4, 5, 6, 7, 8, 0, 1, 2], None, 4)}
        self.assertEqual(4, find_max_depth(node_set))

    def test_find_path(self):
        goal_node = Node([0, 1, 2, 3, 4, 5, 6, 7, 8], Moves.LEFT, 3)
        visited_set = {goal_node,
                       Node([1, 0, 2, 3, 4, 5, 6, 7, 8], Moves.LEFT, 2),
                       Node([1, 2, 0, 3, 4, 5, 6, 7, 8], Moves.UP, 1),
                       Node([1, 2, 5, 3, 4, 0, 6, 7, 8], None, 0),
                       }

        result = find_path(goal_node, visited_set)

        self.assertEqual(visited_set, {goal_node,
                       Node([1, 0, 2, 3, 4, 5, 6, 7, 8], Moves.LEFT, 2),
                       Node([1, 2, 0, 3, 4, 5, 6, 7, 8], Moves.UP, 1),
                       Node([1, 2, 5, 3, 4, 0, 6, 7, 8], None, 0),
                       })
        self.assertEqual(["Up", "Left", "Left"], result)

    def test_find_node_returns_node_when_match_is_found(self):
        previous = Node(self.solved_board, None, 0)
        current = Node(swap(self.solved_board, Moves.RIGHT), Moves.RIGHT, 1)
        visited_set = {previous}
        self.assertEqual(previous, find_node(Node(current.prev_board), visited_set))

    def test_find_node_returns_none_when_no_match_is_found(self):
        other = Node(swap(self.solved_board, Moves.DOWN), Moves.UP, 0)
        current = Node(swap(self.solved_board, Moves.RIGHT), Moves.RIGHT, 1)
        visited_set = {other}
        self.assertEqual(None, find_node(current, visited_set))


if __name__ == '__main__':
    unittest.main()
