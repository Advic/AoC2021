import re
from typing import List
from collections import Counter


class Decoder:
    SEVEN_SEGMENT_MAPPING = {
        frozenset('abcefg'): 0,
        frozenset('cf'): 1,
        frozenset('acdeg'): 2,
        frozenset('acdfg'): 3,
        frozenset('bcdf'): 4,
        frozenset('abdfg'): 5,
        frozenset('abdefg'): 6,
        frozenset('acf'): 7,
        frozenset('abcdefg'): 8,
        frozenset('abcdfg'): 9}

    def __init__(self, cipher: str):
        self.code = dict(zip('abcdefg', [None] * 7))

        # seven_segment_two = re.search(r'\b(\w{2})\b', cipher).groups()
        # assert len(seven_segment_two) == 1
        # seven_segment_two_letters = seven_segment_two[0]

        seven_segment_four = re.search(r'\b(\w{4})\b', cipher).groups()
        assert len(seven_segment_four) == 1
        seven_segment_four_letters = seven_segment_four[0]

        frequencies = {i: [] for i in [4, 6, 7, 8, 9]}
        d = dict(Counter(cipher))
        [frequencies[d[letter]].append(letter) for letter in 'abcdefg']

        assert len(frequencies[4]) == len(frequencies[6]) == len(frequencies[9]) == 1
        assert len(frequencies[7]) == len(frequencies[8]) == 2

        # e, b, and f can be uniquely identified in this manner
        self.code[frequencies[4][0]] = 'e'
        self.code[frequencies[6][0]] = 'b'
        self.code[frequencies[9][0]] = 'f'

        # of the two 7-frequencies (d, g), only d is present in the 4-tuple
        if frequencies[7][0] in seven_segment_four_letters:
            self.code[frequencies[7][0]] = 'd'
            self.code[frequencies[7][1]] = 'g'
        else:
            self.code[frequencies[7][0]] = 'g'
            self.code[frequencies[7][1]] = 'd'

        # of the two 8-frequencies (a, c), only c is present in the 4-tuple
        if frequencies[8][0] in seven_segment_four_letters:
            self.code[frequencies[8][0]] = 'c'
            self.code[frequencies[8][1]] = 'a'
        else:
            self.code[frequencies[8][0]] = 'a'
            self.code[frequencies[8][1]] = 'c'

    def decode(self, digit: str):
        return self.SEVEN_SEGMENT_MAPPING[frozenset(map(self.code.get, digit))]

    def decode_fourdigits(self, digits: List[str]):
        total = 0
        for power, digit in zip(reversed(range(4)), digits):
            total += pow(10, power) * self.decode(digit)
        return total

    @classmethod
    def decipher_and_decode_line(cls, line: str) -> int:
        cipher, coded_digits = line.split(' | ')
        return cls(cipher).decode_fourdigits(coded_digits.split())


if __name__ == '__main__':
    # Part 1 skipped by cheating with regex
    with open('input.txt') as f:
        print(sum([Decoder.decipher_and_decode_line(line.strip()) for line in f.readlines()]))
