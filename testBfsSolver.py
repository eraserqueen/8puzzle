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
        self.assertEqual([], solver.visited)
        self.assertEqual(0, len(solver.fringe))
        self.assertEqual([], solver.result.path_to_goal)

    def test_check_next_node_when_board_has_middle_empty_slot(self):
        solver = BfsSolver(self.board_with_middle_empty_slot)
        starting_node = Node(self.board_with_middle_empty_slot)
        self.assertEqual(deque([starting_node]), solver.fringe)
        solver.check_next_node()
        self.assertEqual(['root'], [str(n) for n in solver.visited])
        self.assertEqual(['1U', '1D', '1L', '1R'], [str(n) for n in solver.fringe])
        solver.check_next_node()
        self.assertEqual(['root', '1U'], [str(n) for n in solver.visited])
        self.assertEqual(['1D', '1L', '1R', '2UD', '2UL', '2UR'], [str(n) for n in solver.fringe])

    def test_run_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        result = solver.run()
        expected = Result()
        self.assertEqual(expected, result)

    def test_run_when_board_is_solved_in_one_move(self):
        starting_board = self.solved_board.down()
        solver = BfsSolver(starting_board)
        solver.run()
        self.assertEqual(0, len(solver.fringe))
        self.assertEqual([Node(starting_board)], solver.visited)
        self.assertEqual(["up"], solver.result.path_to_goal)
        self.assertEqual(1, solver.result.nodes_expanded)
        self.assertEqual(1, solver.result.search_depth)
        self.assertEqual(1, solver.result.max_search_depth)

    def test_run_when_board_is_solved_in_5_moves(self):
        board = Board().down().down().right().right().up();
        solver = BfsSolver(board)
        solver.run()
        solution = ['down', 'left', 'left', 'up', 'up']
        self.assertEqual(solution, solver.result.path_to_goal)
        self.assertEqual(47, solver.result.nodes_expanded)
        self.assertEqual(5, solver.result.search_depth)
        self.assertEqual(5, solver.result.max_search_depth)

    def test_sets_max_depth(self):
        starting_board = self.board_with_middle_empty_slot
        solver = BfsSolver(starting_board)
        self.assertEqual(0, solver.result.max_search_depth)
        solver.check_next_node()
        solver.check_next_node()
        self.assertEqual(1, solver.result.max_search_depth)

    def test_add_to_fringe(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual(deque([Node(self.solved_board)]), solver.fringe)
        solver.add_to_fringe([Node(self.board_with_middle_empty_slot)])
        self.assertEqual(deque([Node(self.solved_board), Node(self.board_with_middle_empty_slot)]), solver.fringe)

    if __name__ == '__main__':
        unittest.main()
