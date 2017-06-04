import unittest

from Moves import *
from bfsSolver import BfsSolver
from node import Node, swap


class TestBfsSolver(unittest.TestCase):
    solved_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board_with_middle_empty_slot = [1, 2, 3, 4, 0, 5, 6, 7, 8]

    def test_init(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual(set(), solver.visited)
        self.assertTrue(Node(self.solved_board) in solver.fringe)
        self.assertEqual([Node(self.solved_board)], solver.fringe)

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

    def test_check_next_node_sets_solution_found(self):
        solver = BfsSolver(self.solved_board)
        solver.fringe.add_all([Node(self.solved_board),
                               Node(swap(self.solved_board, Moves.RIGHT)),
                               Node(swap(self.solved_board, Moves.DOWN))])
        solver.solution_found = False
        solver.check_next_node()
        self.assertTrue(solver.solution_found)

    def test_check_next_node_adds_next_states_to_fringe(self):
        solver = BfsSolver(self.board_with_middle_empty_slot)
        solver.check_next_node()
        self.assertEqual([Node([1, 0, 3, 4, 2, 5, 6, 7, 8], Moves.UP, 2),
                          Node([1, 2, 3, 4, 7, 5, 6, 0, 8], Moves.DOWN, 2),
                          Node([1, 2, 3, 0, 4, 5, 6, 7, 8], Moves.LEFT, 2),
                          Node([1, 2, 3, 4, 5, 0, 6, 7, 8], Moves.RIGHT, 2)],
                         solver.fringe)

    def test_should_add_to_fringe_when_node_is_not_in_fringe_or_visited(self):
        solver = BfsSolver(self.solved_board)
        self.assertEqual([Node(self.solved_board)], solver.fringe)
        self.assertTrue(solver.should_add_to_fringe(Node(self.board_with_middle_empty_slot)))

    def test_should_not_add_to_fringe_when_node_is_in_fringe(self):
        solver = BfsSolver(self.solved_board)
        next_node = Node(self.solved_board)
        self.assertEqual([next_node], solver.fringe)
        self.assertFalse(solver.should_add_to_fringe(next_node))

    def test_should_not_add_to_fringe_when_node_is_visited(self):
        solver = BfsSolver(self.solved_board)
        next_node = Node(self.board_with_middle_empty_slot)
        solver.add_to_visited(next_node)
        self.assertFalse(solver.should_add_to_fringe(next_node))

    def test_fringe_add_board(self):
        solver = BfsSolver(self.solved_board)
        solver.fringe.add(Node(self.board_with_middle_empty_slot))
        self.assertEqual([Node(self.solved_board), Node(self.board_with_middle_empty_slot)], solver.fringe)

    def test_fringe_add_node(self):
        solver = BfsSolver(self.solved_board)
        solver.fringe.add(Node(self.board_with_middle_empty_slot))
        self.assertEqual([Node(self.solved_board), Node(self.board_with_middle_empty_slot)], solver.fringe)
        self.assertEqual({876543210, 876504321}, solver.fringe.hashes)

    def test_fringe_add_all(self):
        solver = BfsSolver(self.solved_board)
        solver.fringe.add_all([Node(self.board_with_middle_empty_slot)])
        self.assertEqual([Node(self.solved_board), Node(self.board_with_middle_empty_slot)], solver.fringe)
        self.assertEqual({876543210, 876504321}, solver.fringe.hashes)

    if __name__ == '__main__':
        unittest.main()
