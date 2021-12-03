#!/usr/bin/env python3

import numpy as np


def depth_scan(depths: np.array) -> int:
    return ((depths[1:] - depths[:-1]) > 0).sum()


def sliding_depth_scan(depth_sums: np.array, window_size: int) -> int:
    depth_sums = np.array([depth_sums[i:len(depth_sums) - (window_size - i) + 1] for i in range(window_size)]).sum(
        axis=0)
    return ((depth_sums[1:] - depth_sums[:-1]) > 0).sum()


if __name__ == '__main__':
    data = np.loadtxt('input.txt')
    print("part A")
    print(depth_scan(data))
    print()
    print("part B")
    print(sliding_depth_scan(data, 3))
