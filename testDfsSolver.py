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

    if __name__ == '__main__':
        unittest.main()
