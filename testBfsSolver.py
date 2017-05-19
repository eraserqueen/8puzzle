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
        self.assertEqual([starting_node], solver.visited)
        self.assertEqual(Node(Board([1, 0, 3, 4, 2, 5, 6, 7, 8]), ["up"]), solver.fringe[0])
        self.assertEqual(Node(Board([1, 2, 3, 4, 7, 5, 6, 0, 8]), ["down"]), solver.fringe[1])
        self.assertEqual(Node(Board([1, 2, 3, 0, 4, 5, 6, 7, 8]), ["left"]), solver.fringe[2])
        self.assertEqual(Node(Board([1, 2, 3, 4, 5, 0, 6, 7, 8]), ["right"]), solver.fringe[3])

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

    if __name__ == '__main__':
        unittest.main()
