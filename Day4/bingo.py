import itertools
from typing import Generator

import numpy as np


def parse_input(lineiter: Generator):
    calls = np.fromstring(next(lineiter), dtype=int, sep=',')
    boards = []
    while True:
        try:
            next(lineiter)
        except StopIteration:
            break
        boards.append(BingoBoard.create_from_str(
            '\n'.join(map(lambda _: next(lineiter), range(BingoBoard.BINGO_BOARD_SIDE_LENGTH)))))
    return calls, boards


class BingoBoard:
    BINGO_BOARD_SIDE_LENGTH = 5
    BINGO_BOARD_SHAPE = np.array((BINGO_BOARD_SIDE_LENGTH, BINGO_BOARD_SIDE_LENGTH))

    def __init__(self, board: np.ndarray, marked=None):
        assert type(board) == np.ndarray
        assert board.dtype == int
        assert (board.shape == self.BINGO_BOARD_SHAPE).all()
        self.board = board
        if marked is None:
            self.marked = np.zeros(self.BINGO_BOARD_SHAPE, dtype=bool)
        else:
            self.marked = marked

    def mark(self, number: int):
        self.marked[np.where(self.board == number)] = True

    def score_board(self):
        assert self.has_bingo
        return np.sum(self.board * np.invert(self.marked))

    @property
    def has_bingo(self) -> bool:
        return np.any(self.marked.sum(axis=0) == self.BINGO_BOARD_SHAPE[0]) | \
               np.any(self.marked.sum(axis=1) == self.BINGO_BOARD_SHAPE[1])

    @classmethod
    def create_from_str(cls, board_str: str):
        return BingoBoard(np.array([np.fromstring(line, sep=' ') for line in board_str.split('\n')], dtype=int))


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def partition(pred, iterable):
    """Use a predicate to partition entries into false entries and true entries"""
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = itertools.tee(iterable)
    return itertools.filterfalse(pred, t1), filter(pred, t2)


def play_bingo(calls, boards):
    found_fastest_board = False
    slowest_board = None

    for callnum, call in enumerate(calls):
        for board in boards:
            board.mark(call)
        losers, winners = map(list, partition(lambda x: x.has_bingo, boards))

        if any(winners) and not found_fastest_board:
            assert len(winners) == 1
            found_fastest_board = True
            print(f"Part A: Fastest board won after round %d" % callnum)
            print(winners[0].score_board() * call)

        if len(losers) == 1 and slowest_board is None:
            slowest_board = losers[0]

        if slowest_board and slowest_board.has_bingo:
            print()
            print(f"Part B: Slowest board won after round %d" % callnum)
            print(slowest_board.score_board() * call)
            break


def file_generator(filename):
    for line in open(filename, 'r'):
        yield line.strip()


if __name__ == '__main__':
    play_bingo(*parse_input(file_generator('input.txt')))
