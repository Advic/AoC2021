#!/usr/bin/env python3

import numpy as np


def depth_scan(depths: np.array) -> int:
    return ((depths[1:] - depths[:-1]) > 0).sum()


if __name__ == '__main__':
    print(depth_scan(np.loadtxt('input.txt')))
