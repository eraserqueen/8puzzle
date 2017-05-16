import unittest
from collections import deque

from src.main.bfsSolver import BfsSolver
from src.main.board import Board
from src.main.node import Node
from src.main.result import Result


class TestBfsSolver(unittest.TestCase):
    solved_board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
    board_with_middle_empty_slot = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])

    def test_init(self):
        solver = BfsSolver(self.solved_board)
        self.assertEquals([], solver.visited)
        self.assertEquals(Result(), solver.result)
        self.assertEquals(Node(self.solved_board), solver.fringe[0])

    def test_check_next_node_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        solver.check_next_node()
        self.assertEquals([], solver.visited)
        self.assertEquals(0, len(solver.fringe))
        self.assertEquals([], solver.result.path_to_goal)

    def test_check_next_node_when_board_has_middle_empty_slot(self):
        solver = BfsSolver(self.board_with_middle_empty_slot)
        starting_node = Node(self.board_with_middle_empty_slot)
        self.assertEquals(deque([starting_node]), solver.fringe)
        solver.check_next_node()
        self.assertEquals([starting_node], solver.visited)
        self.assertEquals(Node(Board([1, 0, 3, 4, 2, 5, 6, 7, 8]), ["up"]), solver.fringe[0])
        self.assertEquals(Node(Board([1, 2, 3, 4, 7, 5, 6, 0, 8]), ["down"]), solver.fringe[1])
        self.assertEquals(Node(Board([1, 2, 3, 0, 4, 5, 6, 7, 8]), ["left"]), solver.fringe[2])
        self.assertEquals(Node(Board([1, 2, 3, 4, 5, 0, 6, 7, 8]), ["right"]), solver.fringe[3])

    def test_run_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        result = solver.run()
        expected = Result()
        self.assertEquals(expected, result)

    def test_run_when_board_is_solved_in_one_move(self):
        starting_board = self.solved_board.down()
        solver = BfsSolver(starting_board)
        solver.run()
        self.assertEquals(0, len(solver.fringe))
        self.assertEquals([Node(starting_board)], solver.visited)
        self.assertEquals(["up"], solver.result.path_to_goal)

    if __name__ == '__main__':
        unittest.main()
