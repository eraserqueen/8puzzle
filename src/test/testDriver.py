import unittest

from src.main.board import Board
from src.main.driver_3 import Driver
from src.main.node import Node
from src.main.result import Result


class TestDriver(unittest.TestCase):
    def test_init(self):
        driver = Driver("bfs", "3,2,4,1,5,7,6,0,8")
        tiles = [3, 2, 4, 1, 5, 7, 6, 0, 8]
        self.assertEquals("BFS", driver.solver.strategy)
        self.assertEquals(Node(Board(tiles)), driver.solver.fringe[0])

    def test_run(self):
        driver = Driver("bfs", "0,1,2,3,4,5,6,7,8")
        result = driver.run()
        expected_result = Result().stringified
        self.assertEquals(expected_result, result)


if __name__ == '__main__':
    unittest.main()
