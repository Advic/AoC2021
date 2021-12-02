import unittest

import numpy as np

from depths import depth_scan


class TestSonarSweep(unittest.TestCase):
    def test_sonar_sweep(self):
        self.assertEqual(depth_scan(np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])), 7)


if __name__ == '__main__':
    unittest.main()
