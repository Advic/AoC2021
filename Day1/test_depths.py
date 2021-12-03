import unittest

import numpy as np

from depths import depth_scan, sliding_depth_scan


class TestSonarSweep(unittest.TestCase):
    def test_depth_scan(self):
        self.assertEqual(depth_scan(np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])), 7)

    def test_sliding_depth_scan(self):
        self.assertEqual(sliding_depth_scan(np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]), 3), 5)


if __name__ == '__main__':
    unittest.main()
