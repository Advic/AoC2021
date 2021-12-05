import textwrap
import unittest

import numpy as np

import vents


class MyTestCase(unittest.TestCase):
    TEST_VENTS = textwrap.dedent("""\
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2""").split('\n')

    VENT_MAP_STRAIGHT_EXPECTED = np.array([
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]])

    VENT_MAP_STRAIGHT_PLUS_DIAG_EXPECTED = np.array([
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
        [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
        [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]])

    def test_parse_line(self):
        self.assertTrue(vents.Ventmap.parse_line("0,9 -> 5,9") == [0, 9, 5, 9])
        self.assertTrue(vents.Ventmap.parse_line("9,4 -> 3,4") == [3, 4, 9, 4])

    def test_parse_straight_lines(self):
        vm = vents.Ventmap()
        vm.parse_straight_lines(self.TEST_VENTS)
        self.assertTrue(np.all(vm.ventmap == self.VENT_MAP_STRAIGHT_EXPECTED))
        self.assertEqual(vm.count_overlap_2(), 5)

    def test_parse_straight_plus_diag_lines(self):
        vm = vents.Ventmap()
        vm.parse_straight_and_diagonal_lines(self.TEST_VENTS)
        print(vm.ventmap)
        self.assertTrue(np.all(vm.ventmap == self.VENT_MAP_STRAIGHT_PLUS_DIAG_EXPECTED))
        self.assertEqual(vm.count_overlap_2(), 12)

    def test_draw_line(self):
        expected = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]])

        vm = vents.Ventmap()
        vm.draw_line(0, 5, 9, 9)
        self.assertTrue(np.all(vm.ventmap == expected))


if __name__ == '__main__':
    unittest.main()
