import unittest

from src.main.board import Board


class TestBoardClass(unittest.TestCase):
    def test_setsState(self):
        board = Board([3, 4, 1, 5, 2, 6, 8, 0, 7])
        self.assertEquals(board.tiles, [3, 4, 1, 5, 2, 6, 8, 0, 7])

    def test_isSolved(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(board.is_solved())


if __name__ == '__main__':
    unittest.main()
