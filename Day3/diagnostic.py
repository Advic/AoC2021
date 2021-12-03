import numpy as np


def create_boolean_array(report: str) -> np.array:
    return np.array([np.array(list(map(lambda x: int(x), list(line)))) for line in report.split('\n')])


def calculate_gamma_rate(report: str) -> int:
    arr = create_boolean_array(report)
    bitstring = ''
    for sum in arr.sum(axis=0):
        assert sum != arr.shape[0] / 2
        if sum > arr.shape[0] / 2:
            bitstring += '1'
        else:
            bitstring += '0'
    return int(bitstring, 2)


def calculate_epsilon_rate(report: str) -> int:
    arr = create_boolean_array(report)
    bitstring = ''
    for sum in arr.sum(axis=0):
        assert sum != arr.shape[0] / 2
        if sum > arr.shape[0] / 2:
            bitstring += '0'
        else:
            bitstring += '1'
    return int(bitstring, 2)


def calculate_power_consumption(report: str) -> int:
    return calculate_gamma_rate(report) * calculate_epsilon_rate(report)


if __name__ == '__main__':
    with open('input.txt') as f:
        report = f.read()

    print(calculate_power_consumption(report))
