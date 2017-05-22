import unittest

from board import Board
from node import Node


class TestNode(unittest.TestCase):
    starting_board = Board()

    def test_init(self):
        node = Node(self.starting_board, ["blah"])
        self.assertEqual(self.starting_board, node.board)
        self.assertEqual(1, node.depth)
        self.assertEqual(["blah"], node.path)

    def test_init_with_defaults(self):
        node = Node(self.starting_board)
        self.assertEqual(self.starting_board, node.board)
        self.assertEqual(0, node.depth)
        self.assertEqual([], node.path)

    def test_str(self):
        self.assertEqual("root", str(Node(self.starting_board)))
        self.assertEqual("1U", str(Node(self.starting_board, ["up"])))
        self.assertEqual("2UL", str(Node(self.starting_board, ["up", "left"])))
        self.assertEqual("3ULL", str(Node(self.starting_board, ["up", "left", "left"])))

    def test_equal(self):
        self.assertEqual(Node(Board()), Node(Board()))
        self.assertNotEqual(None, Node(Board()))
        self.assertNotEqual(Board(), Node(Board()))
        self.assertNotEqual(Node(Board()), Node(Board([1, 2, 3, 4, 5, 6, 7, 8, 0])))

    def test_depth(self):
        self.assertEqual(0, Node(self.starting_board).depth)
        self.assertEqual(1, Node(self.starting_board, ["up"]).depth)
        self.assertEqual(2, Node(self.starting_board, ["up", "left"]).depth)
        self.assertEqual(3, Node(self.starting_board, ["up", "left", "left"]).depth)


if __name__ == '__main__':
    unittest.main()
