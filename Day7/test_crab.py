import unittest

from crab import calculate_best_linear_solution, calculate_best_triangular_solution, parse_input


class TestCrab(unittest.TestCase):
    TEST_INPUT = '16,1,2,0,4,2,7,1,2,14'

    def test_calculate_best_linear_solution(self):
        self.assertEqual(calculate_best_linear_solution(parse_input(self.TEST_INPUT)), 37)

    def test_calculate_best_triangular_solution(self):
        self.assertEqual(calculate_best_triangular_solution(parse_input(self.TEST_INPUT)), 168)


if __name__ == '__main__':
    unittest.main()
