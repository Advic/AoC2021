#!/usr/bin/env python3

import unittest

import numpy as np


def depth_scan(depths) -> int:
    return ((depths[1:] - depths[:-1]) > 0).sum()


class TestSonarSweep(unittest.TestCase):
    def test_sonar_sweep(self):
        self.assertEqual(depth_scan(np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])), 7)


if __name__ == '__main__':
    depths = np.loadtxt('input.txt')
    print(depth_scan(depths))
