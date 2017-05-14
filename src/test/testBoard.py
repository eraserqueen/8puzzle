import unittest

from src.main.board import Board


class TestBoardClass(unittest.TestCase):
    def test_setsState(self):
        board = Board([3, 4, 1, 5, 2, 6, 8, 0, 7])
        self.assertEquals(board.tiles, [3, 4, 1, 5, 2, 6, 8, 0, 7])

    def test_is_solved(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(board.is_solved)

    def test_empty_slot(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEquals(0, board.empty_slot)

    def test_empty_slot(self):
        board = Board([1, 0, 2, 3, 4, 5, 6, 7, 8])
        self.assertEquals(1, board.empty_slot)

    def test_valid_moves(self):
        self.assertEquals(["down", "right"],
                          Board([0, 1, 2,
                                 3, 4, 5,
                                 6, 7, 8]).valid_moves)
        self.assertEquals(["up", "down", "left", "right"],
                          Board([1, 4, 2,
                                 3, 0, 5,
                                 6, 7, 8]).valid_moves)
        self.assertEquals(["up", "left"],
                          Board([2, 1, 8,
                                 3, 4, 5,
                                 6, 7, 0]).valid_moves)

    def test_next_states(self):
        states = Board([1, 2, 3, 4, 0, 5, 6, 7, 8]).next_states
        expected_states = [
            Board([1, 0, 3, 4, 2, 5, 6, 7, 8]),
            Board([1, 2, 3, 4, 7, 5, 6, 0, 8]),
            Board([1, 2, 3, 0, 4, 5, 6, 7, 8]),
            Board([1, 2, 3, 4, 5, 0, 6, 7, 8]),
        ]
        self.assertEquals(expected_states[0].tiles, states[0].tiles)
        self.assertEquals(expected_states[1].tiles, states[1].tiles)
        self.assertEquals(expected_states[2].tiles, states[2].tiles)
        self.assertEquals(expected_states[3].tiles, states[3].tiles)

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
