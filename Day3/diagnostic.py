import numpy as np


def bitstring_to_int(bitstring: str):
    return int(bitstring, 2)


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
    return bitstring_to_int(bitstring)


def calculate_epsilon_rate(report: str) -> int:
    arr = create_boolean_array(report)
    bitstring = ''
    for sum in arr.sum(axis=0):
        assert sum != arr.shape[0] / 2
        if sum > arr.shape[0] / 2:
            bitstring += '0'
        else:
            bitstring += '1'
    return bitstring_to_int(bitstring)


def calculate_power_consumption(report: str) -> int:
    return calculate_gamma_rate(report) * calculate_epsilon_rate(report)


def calculate_oxygen_generator_rating(report: np.array) -> int:
    report_trim = np.copy(report)
    for bitpos in range(report.shape[1]):
        if report_trim.shape[0] == 1:
            break
        frequency_dict = get_frequency_dict(report_trim, bitpos)
        most_common_value = 1 if frequency_dict.get(1) >= frequency_dict.get(0) else 0
        report_trim = report_trim[np.where(report_trim[:, bitpos] == most_common_value), :][0]
    assert report_trim.shape[0] == 1
    assert report_trim.shape[1] == report.shape[1]
    return bitstring_to_int(''.join(map(str, report_trim[0, :].tolist())))


def calculate_co2_scrubber_rating(report: np.array) -> int:
    report_trim = np.copy(report)
    for bitpos in range(report.shape[1]):
        if report_trim.shape[0] == 1:
            break
        frequency_dict = get_frequency_dict(report_trim, bitpos)
        least_common_value = 1 if frequency_dict.get(1) < frequency_dict.get(0) else 0
        report_trim = report_trim[np.where(report_trim[:, bitpos] == least_common_value), :][0]
    assert report_trim.shape[0] == 1
    assert report_trim.shape[1] == report.shape[1]
    return bitstring_to_int(''.join(map(str, report_trim[0, :].tolist())))


def calculate_life_support_rating(report: np.array) -> int:
    return calculate_oxygen_generator_rating(report) * calculate_co2_scrubber_rating(report)


def get_frequency_dict(report: np.array, bitposition: int) -> dict:
    assert report.ndim == 2
    assert np.all(np.logical_xor(report == 0, report == 1))
    return dict(zip(*np.unique(report[:, bitposition], return_counts=True)))


if __name__ == '__main__':
    with open('input.txt') as f:
        report = f.read()

    print("Part 1")
    print(calculate_power_consumption(report))
    print()
    print("Part 2")
    print(calculate_life_support_rating(create_boolean_array(report)))
