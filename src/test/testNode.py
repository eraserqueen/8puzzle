import unittest

from src.main.board import Board
from src.main.node import Node


class TestNode(unittest.TestCase):
    starting_board = Board()

    def test_init(self):
        node = Node(self.starting_board, ["blah"])
        self.assertEquals(self.starting_board, node.board)
        self.assertEquals(1, node.depth)
        self.assertEquals(["blah"], node.path)

    def test_init_with_defaults(self):
        node = Node(self.starting_board)
        self.assertEquals(self.starting_board, node.board)
        self.assertEquals(0, node.depth)
        self.assertEquals([], node.path)

    def test_str(self):
        self.assertEquals("root", str(Node(self.starting_board)))
        self.assertEquals("1U", str(Node(self.starting_board,  ["up"])))
        self.assertEquals("2UL", str(Node(self.starting_board, ["up", "left"])))
        self.assertEquals("3ULL", str(Node(self.starting_board, ["up", "left", "left"])))

    def test_depth(self):
        self.assertEquals(0, Node(self.starting_board).depth)
        self.assertEquals(1, Node(self.starting_board, ["up"]).depth)
        self.assertEquals(2, Node(self.starting_board, ["up", "left"]).depth)
        self.assertEquals(3, Node(self.starting_board, ["up", "left", "left"]).depth)


if __name__ == '__main__':
    unittest.main()
