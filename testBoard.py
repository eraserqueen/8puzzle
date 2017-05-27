import unittest

from board import Board


class TestBoardClass(unittest.TestCase):
    def test_init_defaults_to_solved_board(self):
        board = Board()
        self.assertEqual(board.tiles, [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(board.is_solved)

    def test_init_sets_tiles(self):
        board = Board([3, 4, 1, 5, 2, 6, 8, 0, 7])
        self.assertEqual(board.tiles, [3, 4, 1, 5, 2, 6, 8, 0, 7])

    def test_str(self):
        self.assertEqual("012345678", str(Board()))

    def test_int(self):
        self.assertEqual(12345678, int(Board()))

    def test_equal(self):
        self.assertEqual(Board(), Board())
        self.assertNotEqual(Board(), Board([1,2,3,4,5,6,7,8,0]))

    def test_is_solved(self):
        board = Board()
        self.assertTrue(board.is_solved)

    def test_empty_slot(self):
        board = Board()
        self.assertEqual(0, board.empty_slot)

    def test_empty_slot(self):
        board = Board([1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(1, board.empty_slot)

    # TODO add more test cases
    def test_down(self):
        board = Board([0, 1, 2,
                       3, 4, 5,
                       6, 7, 8]).down()
        expected = Board([3, 1, 2,
                          0, 4, 5,
                          6, 7, 8])
        self.assertEqual(expected, board)

    def test_up(self):
        board = Board([3, 1, 2,
                       0, 4, 5,
                       6, 7, 8]).up()
        expected = Board([0, 1, 2,
                          3, 4, 5,
                          6, 7, 8])
        self.assertEqual(expected, board)

    def test_right(self):
        board = Board([0, 1, 2,
                       3, 4, 5,
                       6, 7, 8]).right()
        expected = Board([1, 0, 2,
                          3, 4, 5,
                          6, 7, 8])
        self.assertEqual(expected, board)

    def test_left(self):
        board = Board([1, 0, 2,
                       3, 4, 5,
                       6, 7, 8]).left()
        expected = Board([0, 1, 2,
                          3, 4, 5,
                          6, 7, 8])
        self.assertEqual(expected, board)

if __name__ == '__main__':
    unittest.main()
