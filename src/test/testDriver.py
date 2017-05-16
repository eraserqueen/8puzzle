import unittest

from src.main.board import Board
from src.main.driver_3 import Driver
from src.main.node import Node


class TestDriver(unittest.TestCase):
    def test_init(self):
        driver = Driver("bfs", "3,2,4,1,5,7,6,0,8")
        tiles = [3, 2, 4, 1, 5, 7, 6, 0, 8]
        self.assertEquals("BFS", driver.solver.strategy)
        self.assertEquals(Node(Board(tiles)), driver.solver.fringe[0])

    def test_run(self):
        driver = Driver("bfs", "0,1,2,3,4,5,6,7,8")
        result = driver.run()
        self.assertEquals([], result.path_to_goal)
        self.assertEquals(0, result.nodes_expanded)
        self.assertEquals(0, result.search_depth)
        self.assertEquals(0, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)


if __name__ == '__main__':
    unittest.main()
