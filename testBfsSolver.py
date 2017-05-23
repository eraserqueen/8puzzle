import unittest
from collections import deque

from bfsSolver import BfsSolver
from board import Board
from node import Node
from result import Result


class TestBfsSolver(unittest.TestCase):
    solved_board = Board()
    board_with_middle_empty_slot = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])

    def test_init(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual([], solver.visited)
        self.assertEqual(Result(), solver.result)
        self.assertEqual(Node(self.solved_board), solver.fringe[0])

    def test_check_next_node_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        solver.check_next_node()
        self.assertEqual([Node(self.solved_board)], solver.visited)
        self.assertEqual(0, len(solver.fringe))
        self.assertEqual([], solver.result.path_to_goal)

    def test_check_next_node_when_board_has_middle_empty_slot(self):
        solver = BfsSolver(self.board_with_middle_empty_slot)
        starting_node = Node(self.board_with_middle_empty_slot)
        self.assertEqual(deque([starting_node]), solver.fringe)
        solver.check_next_node()
        self.assertEqual(['(1) 103425678 up', '(1) 123475608 down', '(1) 123045678 left', '(1) 123450678 right'],
                         [str(n) for n in solver.fringe])
        self.assertEqual(['(0) 123405678 None'], [str(n) for n in solver.visited])

    def test_sets_max_depth(self):
        starting_board = self.board_with_middle_empty_slot
        solver = BfsSolver(starting_board)
        self.assertEqual(0, solver.result.max_search_depth)
        solver.check_next_node()
        solver.check_next_node()
        self.assertEqual(2, solver.result.max_search_depth)

    def test_add_to_fringe(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual(deque([Node(self.solved_board)]), solver.fringe)
        solver.add_to_fringe([Node(self.board_with_middle_empty_slot)])
        self.assertEqual(deque([Node(self.solved_board), Node(self.board_with_middle_empty_slot)]), solver.fringe)

    if __name__ == '__main__':
        unittest.main()
