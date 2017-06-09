import unittest

from astSolver import AstSolver, AstFringe, AstNode, distance_to_goal


class TestDfsSolver(unittest.TestCase):
    board_d0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board_d2a = [3, 1, 2, 0, 4, 5, 6, 7, 8]
    board_d2b = [1, 0, 2, 3, 4, 5, 6, 7, 8]
    board_d4a = [4, 1, 2, 3, 0, 5, 6, 7, 8]
    board_d4b = [2, 1, 0, 3, 4, 5, 6, 7, 8]
    board_d4c = [6, 1, 2, 3, 4, 5, 0, 7, 8]
    board_d6 = [5, 1, 2, 3, 4, 0, 6, 7, 8]
    board_d8 = [8, 1, 2, 3, 4, 5, 6, 7, 0]

    def test_init(self):
        solver = AstSolver(self.board_d6)
        self.assertTrue(isinstance(solver.fringe, AstFringe))
        starting_node = solver.fringe.get_next_node()
        self.assertTrue(isinstance(starting_node, AstNode))
        self.assertEqual(6, starting_node.cost)

    def test_distance_to_goal(self):
        self.assertEqual(0, distance_to_goal(self.board_d0))
        self.assertEqual(2, distance_to_goal(self.board_d2a))
        self.assertEqual(2, distance_to_goal(self.board_d2b))
        self.assertEqual(4, distance_to_goal(self.board_d4a))
        self.assertEqual(4, distance_to_goal(self.board_d4b))
        self.assertEqual(4, distance_to_goal(self.board_d4c))
        self.assertEqual(6, distance_to_goal(self.board_d6))
        self.assertEqual(8, distance_to_goal(self.board_d8))

    def test_cost(self):
        self.assertEqual(0, AstNode(self.board_d0).cost)
        self.assertEqual(2, AstNode(self.board_d0, None, 2).cost)
        self.assertEqual(2, AstNode(self.board_d2a).cost)
        self.assertEqual(3, AstNode(self.board_d2a, None, 1).cost)

    def test_add_to_fringe(self):
        fringe = AstFringe([AstNode(self.board_d4a)])
        fringe.add(AstNode(self.board_d8))
        self.assertEqual([AstNode(self.board_d4a), AstNode(self.board_d8)], fringe)
        fringe.add(AstNode(self.board_d2a))
        self.assertEqual([AstNode(self.board_d2a), AstNode(self.board_d4a), AstNode(self.board_d8)], fringe)
        fringe.add(AstNode(self.board_d2b))
        self.assertEqual([AstNode(self.board_d2b), AstNode(self.board_d2a), AstNode(self.board_d4a), AstNode(self.board_d8)], fringe)

    if __name__ == '__main__':
        unittest.main()
