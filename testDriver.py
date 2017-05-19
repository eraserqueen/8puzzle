import unittest

from driver_3 import Driver


class TestDriver(unittest.TestCase):
    def test_init(self):
        driver = Driver("bfs", "3,2,4,1,5,7,6,0,8")
        tiles = [3, 2, 4, 1, 5, 7, 6, 0, 8]
        self.assertEqual("BFS", driver.solver.strategy)

    def test_run(self):
        driver = Driver("bfs", "0,1,2,3,4,5,6,7,8")
        result = driver.run()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)
        self.assertEqual(0, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)


if __name__ == '__main__':
    unittest.main()
