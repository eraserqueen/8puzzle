import unittest
from collections import deque

from bfsSolver import BfsSolver
from board import Board
from node import Node


class TestBfsSolver(unittest.TestCase):
    solved_board = Board()
    board_with_middle_empty_slot = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])

    def test_init(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual(set(), solver.visited)
        self.assertEqual(Node(self.solved_board), solver.fringe[0])

    def check_next_node_adds_to_visited_set(self):
        solver = BfsSolver(self.solved_board)
        solver.check_next_node()
        self.assertEqual(set([Node(self.solved_board)]), solver.visited)

    def test_run_computes_result_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        result = solver.run()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)

    def test_check_next_node_clears_fringe_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        solver.add_to_fringe([Node(self.solved_board), Node(Board().right()), Node(Board().down())])
        solver.check_next_node()
        self.assertEqual(0, len(solver.fringe))

    def test_check_next_node_adds_next_states_to_fringe(self):
        solver = BfsSolver(self.board_with_middle_empty_slot)
        solver.check_next_node()
        self.assertEqual(['(2) 103425678 up',
                          '(2) 123475608 down',
                          '(2) 123045678 left',
                          '(2) 123450678 right'],
                         [str(n) for n in solver.fringe])

    def test_should_add_to_fringe_when_node_is_not_in_fringe_or_visited(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual(deque([Node(self.solved_board)]), solver.fringe)
        self.assertTrue(solver.should_add_to_fringe(Node(self.board_with_middle_empty_slot)))

    def test_should_not_add_to_fringe_when_node_is_in_fringe(self):
        solver = BfsSolver(self.solved_board)
        next_node = Node(self.solved_board)
        self.assertEqual(deque([next_node]), solver.fringe)
        self.assertFalse(solver.should_add_to_fringe(next_node))

    def test_should_not_add_to_fringe_when_node_is_visited(self):
        solver = BfsSolver(self.solved_board)
        next_node = Node(self.board_with_middle_empty_slot)
        solver.add_to_visited(next_node)
        self.assertFalse(solver.should_add_to_fringe(next_node))

    def test_add_to_fringe(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual(deque([Node(self.solved_board)]), solver.fringe)
        solver.add_to_fringe([Node(self.board_with_middle_empty_slot)])
        self.assertEqual(deque([Node(self.solved_board), Node(self.board_with_middle_empty_slot)]), solver.fringe)


    if __name__ == '__main__':
        unittest.main()
