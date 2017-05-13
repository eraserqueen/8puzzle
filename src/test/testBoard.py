import unittest

from src.main.board import Board


class TestBoardClass(unittest.TestCase):
    def test_setsState(self):
        board = Board([3, 4, 1, 5, 2, 6, 8, 0, 7])
        self.assertEquals(board.tiles, [3, 4, 1, 5, 2, 6, 8, 0, 7])

    def test_is_solved(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(board.is_solved())

    def test_empty_slot(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEquals(0, board.empty_slot)

    def test_empty_slot(self):
        board = Board([1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEquals(1, board.empty_slot)

    # TODO add more test cases
    def test_down(self):
        board = Board([0, 1, 2,
                       3, 4, 5,
                       6, 7, 8])
        board.down()
        expected = Board([3, 1, 2,
                          0, 4, 5,
                          6, 7, 8])
        self.assertEquals(expected.tiles, board.tiles)

    def test_up(self):
        board = Board([3, 1, 2,
                       0, 4, 5,
                       6, 7, 8])
        board.up()
        expected = Board([0, 1, 2,
                          3, 4, 5,
                          6, 7, 8])
        self.assertEquals(expected.tiles, board.tiles)

    def test_right(self):
        board = Board([0, 1, 2,
                       3, 4, 5,
                       6, 7, 8])
        board.right()
        expected = Board([1, 0, 2,
                          3, 4, 5,
                          6, 7, 8])
        self.assertEquals(expected.tiles, board.tiles)

    def test_left(self):
        board = Board([1, 0, 2,
                       3, 4, 5,
                       6, 7, 8])
        board.left()
        expected = Board([0, 1, 2,
                          3, 4, 5,
                          6, 7, 8])
        self.assertEquals(expected.tiles, board.tiles)


if __name__ == '__main__':
    unittest.main()
