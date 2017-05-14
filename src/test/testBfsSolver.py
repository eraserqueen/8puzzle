import unittest
from collections import deque

from src.main.bfsSolver import BfsSolver
from src.main.board import Board
from src.main.node import Node


class TestBfsSolver(unittest.TestCase):
    solved_board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
    board_with_middle_empty_slot = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])

    def test_init(self):
        solver = BfsSolver(self.solved_board)
        self.assertEquals(Node(self.solved_board), solver.fringe[0])

    def test_check_next_node_when_board_is_solved(self):
        solver = BfsSolver(self.solved_board)
        self.assertEquals(Node(self.solved_board), solver.fringe[0])
        solver.check_next_node()
        self.assertEquals(0, len(solver.fringe))

    def test_check_next_node_when_board_has_middle_empty_slot(self):
        solver = BfsSolver(self.board_with_middle_empty_slot)
        starting_node = Node(self.board_with_middle_empty_slot)
        self.assertEquals(deque([starting_node]), solver.fringe)
        solver.check_next_node()
        self.assertEquals([starting_node], solver.visited)
        self.assertEquals(deque([
            Node(Board([1, 0, 3, 4, 2, 5, 6, 7, 8]), 1, ["up"]),
            Node(Board([1, 2, 3, 4, 7, 5, 6, 0, 8]), 1, ["down"]),
            Node(Board([1, 2, 3, 0, 4, 5, 6, 7, 8]), 1, ["left"]),
            Node(Board([1, 2, 3, 4, 5, 0, 6, 7, 8]), 1, ["right"])
        ]), solver.fringe)


if __name__ == '__main__':
    unittest.main()
