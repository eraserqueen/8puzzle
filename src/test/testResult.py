import unittest

from result import Result


class TestResult(unittest.TestCase):
    def test_init(self):
        result = Result()
        self.assertEqual([], result.path_to_goal)
        self.assertEqual(0, result.cost_of_path)
        self.assertEqual(0, result.nodes_expanded)
        self.assertEqual(0, result.search_depth)
        self.assertEqual(0, result.max_search_depth)
        self.assertEqual(0, result.running_time)
        self.assertEqual(0, result.max_ram_usage)

    def test_str(self):
        result = Result()
        expected = 'path_to_goal: []\n' + \
                   'cost_of_path: 0\n' + \
                   'nodes_expanded: 0\n' + \
                   'search_depth: 0\n' + \
                   'max_search_depth: 0\n' + \
                   'running_time: 0\n' + \
                   'max_ram_usage: 0'
        self.assertEqual(expected, str(result))


if __name__ == '__main__':
    unittest.main()
