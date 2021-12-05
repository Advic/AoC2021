import re
from typing import List

import numpy as np


class Ventmap:
    def __init__(self):
        self.ventmap = np.zeros((0, 0))

    @staticmethod
    def parse_line(line) -> List[int]:
        x1, y1, x2, y2 = list(map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups()))
        if x1 > x2 or y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        return [x1, y1, x2, y2]

    def parse_straight_lines(self, lines: List[str]) -> np.array:
        for line in lines:
            x1, y1, x2, y2 = self.parse_line(line)
            self.draw_line(x1, x2, y1, y2)

    def parse_straight_and_diagonal_lines(self, lines: List[str]) -> np.array:
        for line in lines:
            x1, y1, x2, y2 = self.parse_line(line)
            self.draw_line(x1, x2, y1, y2, draw_diagonals=True)

    def expand_ventmap(self, x1, x2, y1, y2):
        # make ventmap bigger by creating a new zeros array and embedding the existing ventmap in
        maxdim = max(x1, x2, y1, y2) + 1
        if maxdim > self.ventmap.shape[0]:
            tmp = np.zeros((maxdim, maxdim))
            tmp[:self.ventmap.shape[0], :self.ventmap.shape[1]] = self.ventmap
            self.ventmap = tmp

    def draw_line(self, x1, x2, y1, y2, draw_diagonals=False):
        self.expand_ventmap(x1, x2, y1, y2)

        # Skip diagonals
        if x1 != x2 and y1 != y2:
            if not draw_diagonals:
                return
            else:
                self.draw_diagonal_line(x1, x2, y1, y2)
        else:
            self.draw_straight_line(x1, x2, y1, y2)

    def draw_straight_line(self, x1, x2, y1, y2):
        assert x1 <= x2 and y1 <= y2
        if x1 == x2:
            self.ventmap[y1:y2 + 1, x1] += 1
        elif y1 == y2:
            self.ventmap[y1, x1:x2 + 1] += 1
        else:
            assert False

    def draw_diagonal_line(self, x1, x2, y1, y2):
        assert x1 != x2 and y1 != y2
        assert abs(x1 - x2) == abs(y1 - y2)

        if x2 > x1:
            xs = range(x1, x2 + 1)
        else:
            xs = reversed(range(x2, x1 + 1))

        if y2 > y1:
            ys = range(y1, y2 + 1)
        else:
            ys = reversed(range(y2, y1 + 1))

        for x, y in zip(xs, ys):
            self.ventmap[y, x] += 1

    def count_overlap_2(self):
        return (self.ventmap >= 2).sum()


if __name__ == '__main__':
    vm = Ventmap()
    vm.parse_straight_lines(open('input.txt').readlines())
    print(vm.ventmap)
    print("Part A")
    print(vm.count_overlap_2())

    vm = Ventmap()
    vm.parse_straight_and_diagonal_lines(open('input.txt').readlines())
    print(vm.ventmap)
    print("Part B")
    print(vm.count_overlap_2())
