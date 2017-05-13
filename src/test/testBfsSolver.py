import unittest

from src.main.bfsSolver import BfsSolver
from src.main.board import Board


class TestBfsSolver(unittest.TestCase):
    def test_init(self):
        startingState = Board([0,1,2,3,4,5,6,7,8])
        solver = BfsSolver(startingState)
        self.assertEquals(startingState, solver.state)


if __name__ == '__main__':
    unittest.main()