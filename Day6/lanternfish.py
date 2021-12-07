import collections
import itertools
from typing import List


class LanternFishSchool:
    def __init__(self, timers: List[int]):
        self.school = list(map(LanternFish, timers))

    def simulate(self):
        self.school.extend([LanternFish(8) for fish in self.school if fish.simulate()])

    def count(self):
        return len(self.school)

    @classmethod
    def parse_state(cls, state: str):
        return cls(list(map(int, state.split(','))))


class EfficientLanternFishSchool:
    MAX_AGE = 8

    def __init__(self, timers: List[int]):
        self.school = dict(zip(range(self.MAX_AGE + 1), itertools.repeat(0)))
        self.school.update(dict(collections.Counter(timers)))

    def simulate(self):
        num_spawners = self.school[0]
        for timerval in range(self.MAX_AGE):
            self.school[timerval] = self.school[timerval + 1]
        self.school[8] = num_spawners
        self.school[6] += num_spawners

    def count(self):
        return sum(self.school.values())

    @classmethod
    def parse_state(cls, state: str):
        return cls(list(map(int, state.split(','))))


class LanternFish:
    def __init__(self, timer: int):
        self.timer = timer

    def simulate(self) -> bool:
        if self.timer > 0:
            self.timer -= 1
            return False
        if self.timer == 0:
            self.timer = 6
            return True
        else:
            assert False


if __name__ == '__main__':
    with open('input.txt') as f:
        school = EfficientLanternFishSchool.parse_state(f.read())
    for i in range(80):
        school.simulate()
    print("Part A")
    print(school.count())

    with open('input.txt') as f:
        school = EfficientLanternFishSchool.parse_state(f.read())
    for i in range(256):
        school.simulate()
    print("Part B")
    print(school.count())
