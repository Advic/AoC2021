import numpy as np


def parse_input(inp: str) -> np.array:
    return np.array(list(map(int, inp.split(','))))


def calculate_linear_distance(arr: np.array, best_sol: int) -> int:
    return sum(np.abs(arr - best_sol))


def calculate_best_linear_solution(arr: np.array) -> int:
    solns = dict()
    for i in range(arr.min(), arr.max()):
        solns[calculate_linear_distance(arr, i)] = i
    return min(solns.keys())


def calculate_triangular_distance(arr: np.array, best_sol: int) -> int:
    n = abs(arr - best_sol)
    return int(sum((n ** 2 + n) / 2))


def calculate_best_triangular_solution(arr: np.array) -> int:
    solns = dict()
    for i in range(arr.min(), arr.max() + 1):
        solns[calculate_triangular_distance(arr, i)] = i
    return min(solns.keys())


if __name__ == '__main__':
    with open('input.txt') as f:
        print(calculate_best_linear_solution(parse_input(f.read())))

    with open('input.txt') as f:
        print(calculate_best_triangular_solution(parse_input(f.read())))
