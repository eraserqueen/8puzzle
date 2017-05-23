import unittest
from collections import deque

from dfsSolver import DfsSolver
from board import Board
from node import Node


class TestDfsSolver(unittest.TestCase):
    solved_board = Board()
    board_with_middle_empty_slot = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])

    def test_add_to_fringe(self):
        solver = DfsSolver(self.solved_board)
        self.assertEqual(deque([Node(self.solved_board)]), solver.fringe)
        solver.add_to_fringe([Node(self.board_with_middle_empty_slot)])
        self.assertEqual(deque([Node(self.board_with_middle_empty_slot), Node(self.solved_board)]), solver.fringe)

    def test_check_next_node_when_board_has_middle_empty_slot(self):
        solver = DfsSolver(self.board_with_middle_empty_slot)
        starting_node = Node(self.board_with_middle_empty_slot)
        self.assertEqual(deque([starting_node]), solver.fringe)
        solver.check_next_node()
        self.assertEqual(['root'], [str(n) for n in solver.visited])
        self.assertEqual(['1U', '1D', '1L', '1R'], [str(n) for n in solver.fringe])
        solver.check_next_node()
        self.assertEqual(['root', '1U'], [str(n) for n in solver.visited])
        self.assertEqual(['2UD', '2UL', '2UR', '1D', '1L', '1R'], [str(n) for n in solver.fringe])

    if __name__ == '__main__':
        unittest.main()
