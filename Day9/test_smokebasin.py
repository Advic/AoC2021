import unittest

import numpy as np

import smokebasin


class TestSmokeBasin(unittest.TestCase):
    HEIGHTMAP = np.array([[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                          [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                          [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                          [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                          [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])

    def test_smoke_basin(self):
        basin = smokebasin.SmokeBasin(self.HEIGHTMAP)
        self.assertEqual(15, basin.sum_risk_levels())

    def test_segment_image(self):
        segmented_basins = smokebasin.SmokeBasin(self.HEIGHTMAP).segment_basins()
        self.assertTrue(np.all(segmented_basins == np.array([
            [1, 1, 0, 0, 0, 2, 2, 2, 2, 2],
            [1, 0, 3, 3, 3, 0, 2, 0, 2, 2],
            [0, 3, 3, 3, 3, 3, 0, 4, 0, 2],
            [3, 3, 3, 3, 3, 0, 4, 4, 4, 0],
            [0, 3, 0, 0, 0, 4, 4, 4, 4, 4]])))


if __name__ == '__main__':
    unittest.main()
