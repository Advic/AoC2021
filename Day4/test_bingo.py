import textwrap
import unittest

import numpy as np

import bingo


class MyTestCase(unittest.TestCase):
    CALLS = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    TEST_BOARD_1 = np.array([
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19]])
    TEST_BOARD_2 = np.array([
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6]])

    TEST_BOARD_3 = np.array([
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7]])

    LOSING_MARKS = np.array([
        [True, True, True, True, False],
        [False, False, False, True, False],
        [False, False, True, True, False],
        [False, True, False, False, True],
        [True, True, False, False, True]
    ])

    WINNING_MARKS = np.array([
        [True, True, True, True, True],
        [False, False, False, True, False],
        [False, False, True, False, False],
        [False, True, False, False, True],
        [True, True, False, False, True]
    ])

    def test_has_bingo(self):
        self.assertFalse(bingo.BingoBoard(self.TEST_BOARD_3, self.LOSING_MARKS).has_bingo)
        self.assertTrue(bingo.BingoBoard(self.TEST_BOARD_3, self.WINNING_MARKS).has_bingo)

    def test_score_board(self):
        self.assertEqual(bingo.BingoBoard(self.TEST_BOARD_3, self.WINNING_MARKS).score_board(), 188)

    def test_mark(self):
        board_1 = bingo.BingoBoard(self.TEST_BOARD_1)
        board_2 = bingo.BingoBoard(self.TEST_BOARD_2)
        board_3 = bingo.BingoBoard(self.TEST_BOARD_3)
        boards = [board_1, board_2, board_3]
        for call in [7, 4, 9, 5, 11]:
            for board in boards:
                board.mark(call)
        self.assertTrue(np.all(board_1.marked == np.array([
            [False, False, False, True, False],
            [False, False, False, True, False],
            [False, True, False, False, True],
            [False, False, False, False, True],
            [False, False, False, False, False]])))
        self.assertTrue(np.all(board_2.marked == np.array([
            [False, False, False, False, False],
            [True, False, False, False, True],
            [False, False, True, False, False],
            [False, True, False, False, True],
            [False, False, False, False, False]])))
        self.assertTrue(np.all(board_3.marked == np.array([
            [False, False, False, False, True],
            [False, False, False, True, False],
            [False, False, False, False, False],
            [False, True, False, False, True],
            [False, False, False, False, True]])))

    def test_factory(self):
        bingo_board_str = textwrap.dedent("""\
        22 13 17 11  0
         8  2 23  4 24
        21  9 14 16  7
         6 10  3 18  5
         1 12 20 15 19""")

        self.assertTrue(np.all(bingo.BingoBoard.create_from_str(bingo_board_str).board == self.TEST_BOARD_1))


if __name__ == '__main__':
    unittest.main()
