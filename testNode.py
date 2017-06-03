import unittest

from Moves import *
from node import Node


class TestNode(unittest.TestCase):
    starting_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def test_init(self):
        node = Node(self.starting_board, Moves.UP, 4)
        self.assertEqual(self.starting_board, node.board)
        self.assertEqual(Moves.UP, node.origin)
        self.assertEqual(4, node.depth)

    def test_init_with_defaults(self):
        node = Node(self.starting_board)
        self.assertEqual(self.starting_board, node.board)
        self.assertEqual(1, node.depth)
        self.assertEqual(None, node.origin)

    def test_str(self):
        self.assertEqual("(1) 012345678 None", str(Node(self.starting_board)))
        self.assertEqual("(3) 012345678 -3", str(Node(self.starting_board, Moves.UP, 3)))

    def test_hash(self):
        self.assertEqual(12345678, hash(Node(self.starting_board)))
        self.assertEqual(12345678, hash(Node(self.starting_board, Moves.UP, 3)))

    def test_equal(self):
        self.assertEqual(Node(self.starting_board), Node([0, 1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(Node(self.starting_board), Node(self.starting_board))
        self.assertEqual(Node(self.starting_board, Moves.UP, 3), Node(self.starting_board))
        self.assertEqual(Node(self.starting_board, Moves.DOWN, 1), Node(self.starting_board, Moves.UP, 3))
        self.assertNotEqual(None, Node(self.starting_board))
        self.assertNotEqual(Node(self.starting_board), Node([1, 2, 3, 4, 5, 6, 7, 8, 0]))

    def test_next_states_when_empty_slot_is_in_the_center(self):
        starting_node = Node([1, 2, 3, 4, 0, 5, 6, 7, 8])
        states = starting_node.next_states
        expected_states = [
            Node([1, 0, 3, 4, 2, 5, 6, 7, 8], Moves.UP, 1),
            Node([1, 2, 3, 4, 7, 5, 6, 0, 8], Moves.DOWN, 1),
            Node([1, 2, 3, 0, 4, 5, 6, 7, 8], Moves.LEFT, 1),
            Node([1, 2, 3, 4, 5, 0, 6, 7, 8], Moves.RIGHT, 1),
        ]
        self.assertEqual(expected_states, states)

    def test_next_states_when_empty_slot_is_in_a_corner(self):
        states = Node(self.starting_board).next_states
        expected_states = [
            Node([3, 1, 2, 0, 4, 5, 6, 7, 8], Moves.DOWN, 1),
            Node([1, 0, 2, 3, 4, 5, 6, 7, 8], Moves.RIGHT, 1)
        ]
        self.assertEqual(expected_states, states)

    def test_prev_state(self):
        current = Node([3, 1, 2, 0, 4, 5, 6, 7, 8], Moves.DOWN, 1)
        self.assertEqual(self.starting_board, current.prev_board)


if __name__ == '__main__':
    unittest.main()
