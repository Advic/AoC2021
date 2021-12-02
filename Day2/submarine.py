#!/usr/bin/env python3.10

class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, d):
        self.x += d

    def down(self, d):
        self.y -= d

    def up(self, d):
        self.y += d

    @property
    def score(self):
        return abs(self.x * self.y)

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


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    sub = Submarine()
    for line in lines:
        sub.parse(line)

    print(sub.score)
