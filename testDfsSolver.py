import unittest

from dfsSolver import DfsSolver
from node import Node


class TestDfsSolver(unittest.TestCase):
    solved_board = [0,1,2,3,4,5,6,7,8]
    board_with_middle_empty_slot = [1, 2, 3, 4, 0, 5, 6, 7, 8]

    def test_add_to_fringe(self):
        solver = DfsSolver(self.solved_board)
        self.assertEqual([Node(self.solved_board)], solver.fringe)
        solver.fringe.add_all([Node(self.board_with_middle_empty_slot)])
        expected_fringe = [Node(self.board_with_middle_empty_slot), Node(self.solved_board)]
        self.assertEqual(expected_fringe, solver.fringe)

    if __name__ == '__main__':
        unittest.main()
