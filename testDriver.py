import unittest

from driver_3 import Driver


class TestDriver(unittest.TestCase):
    def test_init(self):
        driver = Driver("bfs", "3,2,4,1,5,7,6,0,8")
        self.assertEqual("BFS", driver.solver.strategy)

    def test_run_with_bfs_solved(self):
        driver = Driver("bfs", "0,1,2,3,4,5,6,7,8")
        result = driver.run()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.cost_of_path)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)
        self.assertEqual(0, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)

    def test_run_with_bfs_case_1(self):
        driver = Driver("bfs", "1,2,5,3,4,0,6,7,8")
        result = driver.run()
        self.assertEqual(['Up', 'Left', 'Left'], result.path_to_goal)
        self.assertEqual(3, result.cost_of_path)
        self.assertEqual(10, result.nodes_expanded)
        self.assertEqual(3, result.search_depth)
        self.assertEqual(4, result.max_search_depth)

    def test_run_with_bfs_case_2(self):
        driver = Driver("bfs", "6,1,8,4,0,2,7,3,5")
        result = driver.run()
        self.assertEqual(['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right',
                          'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right',
                          'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], result.path_to_goal)
        self.assertEqual(20, result.cost_of_path)
        self.assertEqual(54094, result.nodes_expanded)
        self.assertEqual(20, result.search_depth)
        self.assertEqual(21, result.max_search_depth)

    def test_run_with_bfs_case_3(self):
        driver = Driver("bfs", "8,6,4,2,1,3,5,7,0")
        result = driver.run()
        self.assertEqual(['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down',
                          'Left', 'Up', 'Right', 'Right', 'Up', 'Left',
                          'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down',
                          'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], result.path_to_goal)
        self.assertEqual(26, result.cost_of_path)
        self.assertEqual(166786, result.nodes_expanded)
        self.assertEqual(26, result.search_depth)
        self.assertEqual(27, result.max_search_depth)

    def test_run_with_dfs_solved(self):
        driver = Driver("dfs", "0,1,2,3,4,5,6,7,8")
        result = driver.run()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.cost_of_path)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)
        self.assertEqual(0, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)

    def test_run_with_dfs_case_1(self):
        driver = Driver("dfs", "1,2,5,3,4,0,6,7,8")
        result = driver.run()
        self.assertEqual(['Up', 'Left', 'Left'], result.path_to_goal)
        self.assertEqual(3, result.cost_of_path)
        self.assertEqual(181437, result.nodes_expanded)
        self.assertEqual(3, result.search_depth)
        self.assertEqual(66125, result.max_search_depth)

    @unittest.skip
    def test_run_with_dfs_case_2(self):
        driver = Driver("dfs", "6,1,8,4,0,2,7,3,5")
        result = driver.run()
        self.assertEqual(['Up', 'Left', 'Down'], result.path_to_goal[0:3])
        self.assertEqual(['Up', 'Left', 'Up', 'Left'], result.path_to_goal[len(result.path_to_goal) - 4:])
        self.assertEqual(46142, result.cost_of_path)
        self.assertEqual(51015, result.nodes_expanded)
        self.assertEqual(46142, result.search_depth)
        self.assertEqual(46142, result.max_search_depth)

    @unittest.skip
    def test_run_with_dfs_case_3(self):
        driver = Driver("dfs", "8,6,4,2,1,3,5,7,0")
        result = driver.run()
        self.assertEqual(['Up', 'Up', 'Left'], result.path_to_goal[0:3])
        self.assertEqual(['Up', 'Up', 'Left'], result.path_to_goal[len(result.path_to_goal) - 3:])
        self.assertEqual(9612, result.cost_of_path)
        self.assertEqual(9869, result.nodes_expanded)
        self.assertEqual(9612, result.search_depth)
        self.assertEqual(9612, result.max_search_depth)

    def test_run_with_ast_solved(self):
        driver = Driver("ast", "0,1,2,3,4,5,6,7,8")
        result = driver.run()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.cost_of_path)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)
        self.assertEqual(0, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)

    def test_run_with_ast_case1(self):
        driver = Driver("ast", "6,1,8,4,0,2,7,3,5")
        result = driver.run()
        self.assertEqual(['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], result.path_to_goal)
        self.assertEqual(20, result.cost_of_path)
        self.assertEqual(696, result.nodes_expanded)
        self.assertEqual(20, result.search_depth)
        self.assertEqual(20, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)

    def test_run_with_ast_case2(self):
        driver = Driver("ast", "8,6,4,2,1,3,5,7,0")
        result = driver.run()
        self.assertEqual(['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], result.path_to_goal)
        self.assertEqual(26, result.cost_of_path)
        self.assertEqual(1585, result.nodes_expanded)
        self.assertEqual(26, result.search_depth)
        self.assertEqual(26, result.max_search_depth)
        self.assertTrue(result.running_time > 0)
        self.assertTrue(result.max_ram_usage > 0)

if __name__ == '__main__':
    unittest.main()
