import unittest

from src.main.result import Result

class TestResult(unittest.TestCase):
    def test_init(self):
        result = Result()
        self.assertEquals([], result.path_to_goal)
        self.assertEquals(0, result.cost_of_path)
        self.assertEquals(0, result.nodes_expanded)
        self.assertEquals(0, result.search_depth)
        self.assertEquals(0, result.max_search_depth)
        self.assertEquals(0, result.running_time)
        self.assertEquals(0, result.max_ram_usage)

    def test_stringify(self):
        result = Result()
        expected = """path_to_goal: []
cost_of_path: 0
nodes_expanded: 0
search_depth: 0
max_search_depth: 0
running_time: 0
max_ram_usage: 0"""
        self.assertEquals(expected, result.stringified)

if __name__ == '__main__':
    unittest.main()
