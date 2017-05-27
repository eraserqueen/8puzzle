import unittest

from board import Board
from node import Node


class TestNode(unittest.TestCase):
    starting_board = Board()

    def test_init(self):
        node = Node(self.starting_board, "up", 4)
        self.assertEqual(self.starting_board, node.board)
        self.assertEqual("up", node.origin)
        self.assertEqual(4, node.depth)

    def test_init_with_defaults(self):
        node = Node(self.starting_board)
        self.assertEqual(self.starting_board, node.board)
        self.assertEqual(0, node.depth)
        self.assertEqual(None, node.origin)
        self.assertEqual(0, node.depth)

    def test_str(self):
        self.assertEqual("(0) 012345678 None", str(Node(self.starting_board)))
        self.assertEqual("(3) 012345678 up", str(Node(self.starting_board, "up", 3)))

    def test_hash(self):
        self.assertEqual(12345678, hash(Node(self.starting_board)))
        self.assertEqual(12345678, hash(Node(self.starting_board, "up", 3)))

    def test_equal(self):
        self.assertEqual(Node(Board()), Node(Board()))
        self.assertEqual(Node(self.starting_board), Node(Board()))
        self.assertEqual(Node(self.starting_board, "up", 3), Node(Board()))
        self.assertEqual(Node(self.starting_board, "down", 1), Node(self.starting_board, "up", 3))
        self.assertNotEqual(None, Node(Board()))
        self.assertNotEqual(Board(), Node(Board()))
        self.assertNotEqual(Node(Board()), Node(Board([1, 2, 3, 4, 5, 6, 7, 8, 0])))

    def test_valid_moves(self):
        self.assertEqual(["down", "right"],
                         Node(Board([0, 1, 2,
                                     3, 4, 5,
                                     6, 7, 8])).valid_moves)
        self.assertEqual(["up", "down", "left", "right"],
                         Node(Board([1, 4, 2,
                                     3, 0, 5,
                                     6, 7, 8])).valid_moves)
        self.assertEqual(["up", "left"],
                         Node(Board([2, 1, 8,
                                     3, 4, 5,
                                     6, 7, 0])).valid_moves)

    def test_next_states_when_empty_slot_is_in_the_center(self):
        states = Node(Board([1, 2, 3, 4, 0, 5, 6, 7, 8])).next_states
        expected_states = [
            Node(Board([1, 0, 3, 4, 2, 5, 6, 7, 8]), "up", 1),
            Node(Board([1, 2, 3, 4, 7, 5, 6, 0, 8]), "down", 1),
            Node(Board([1, 2, 3, 0, 4, 5, 6, 7, 8]), "left", 1),
            Node(Board([1, 2, 3, 4, 5, 0, 6, 7, 8]), "right", 1),
        ]
        self.assertEqual(expected_states, states)

    def test_next_states_when_empty_slot_is_in_a_corner(self):
        states = Node(Board()).next_states
        expected_states = [
            Node(Board([3, 1, 2, 0, 4, 5, 6, 7, 8]), "down", 1),
            Node(Board([1, 0, 2, 3, 4, 5, 6, 7, 8]), "right", 1)
        ]
        self.assertEqual(expected_states, states)


if __name__ == '__main__':
    unittest.main()
