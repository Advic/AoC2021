#!/usr/bin/env python3.10

class Submarine:
    def __init__(self):
        self.position = 0
        self.depth = 0

    def forward(self, d):
        self.position += d

    def down(self, d):
        self.depth += d

    def up(self, d):
        self.depth -= d

    @property
    def score(self):
        return abs(self.position * self.depth)

    def parse(self, command: str):
        action, num = command.split(' ', 1)
        d = int(num)
        assert d > 0
        match action:
            case 'forward':
                self.forward(d)
            case 'up':
                self.up(d)
            case 'down':
                self.down(d)
            case _:
                raise Exception("Unknown command")


class AimingSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, d):
        self.position += d
        self.depth += self.aim * d

    def down(self, d):
        self.aim += d

    def up(self, d):
        self.aim -= d


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    print("Part A")
    sub = Submarine()
    for line in lines:
        sub.parse(line)
    print(sub.score)

    print("Part B")
    aimingsub = AimingSubmarine()
    for line in lines:
        aimingsub.parse(line)
    print(aimingsub.score)
