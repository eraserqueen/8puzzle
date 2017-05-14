import unittest

from src.main.bfsSolver import BfsSolver
from src.main.board import Board


class TestBfsSolver(unittest.TestCase):
    def test_init(self):
        startingState = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        solver = BfsSolver(startingState)
        self.assertEquals(startingState, solver.state)

    def test_next_states(self):
        board = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])
        solver = BfsSolver(board)
        expected_states = [
            Board([1, 0, 3, 4, 2, 5, 6, 7, 8]),
            Board([1, 2, 3, 4, 7, 5, 6, 0, 8]),
            Board([1, 2, 3, 0, 4, 5, 6, 7, 8]),
            Board([1, 2, 3, 4, 5, 0, 6, 7, 8]),
        ]
        next_states = solver.next_states(board)
        self.assertEquals(expected_states[0].tiles, next_states[0].tiles)
        self.assertEquals(expected_states[1].tiles, next_states[1].tiles)
        self.assertEquals(expected_states[2].tiles, next_states[2].tiles)
        self.assertEquals(expected_states[3].tiles, next_states[3].tiles)

if __name__ == '__main__':
    unittest.main()
