import unittest

from bfsSolver import Fringe
from node import Node


class TestFringe(unittest.TestCase):
    
    starting_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    def test_init(self):
        empty_fringe = Fringe()
        fringe_with_node = Fringe([Node(self.starting_board)])
        self.assertEqual(len(empty_fringe.queue), 0)
        self.assertEqual(len(fringe_with_node.queue), 1)

    def test_clear(self):
        fringe_with_node = Fringe([Node(self.starting_board)])
        fringe_with_node.clear()
        self.assertEqual(0, len(fringe_with_node.queue))

    def test_has_nodes(self):
        empty_fringe = Fringe()
        fringe_with_node = Fringe([Node(self.starting_board)])
        self.assertFalse(empty_fringe.has_nodes())
        self.assertTrue(fringe_with_node.has_nodes())

    def test_get_next_node(self):
        fringe_with_node = Fringe([Node(self.starting_board)])
        self.assertEqual(Node(self.starting_board), fringe_with_node.get_next_node())

    def test_contains(self):
        empty_fringe = Fringe()
        fringe_with_node = Fringe([Node(self.starting_board)])
        self.assertTrue(Node(self.starting_board) in fringe_with_node)
        self.assertFalse(Node(self.starting_board) in empty_fringe)

    def test_equality(self):
        self.assertEqual(Fringe(), Fringe())
        self.assertEqual(Fringe([Node(self.starting_board)]), Fringe([Node(self.starting_board)]))
        self.assertEqual(Fringe([Node(self.starting_board)]), [Node(self.starting_board)])

    if __name__ == '__main__':
        unittest.main()
