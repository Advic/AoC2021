import numpy as np


class DumboOctopi:
    def __init__(self, energylevels: np.array):
        self.energylevels = np.array(energylevels)
        self.numflashes = 0

    def iterate(self, numiterations=1):
        for i in range(numiterations):
            self.energylevels += 1
            flashed = np.zeros(self.energylevels.shape, dtype=bool)
            ys, xs = np.where((self.energylevels > 9) * ~flashed)
            while len(ys) > 0:
                flashed = self.energylevels > 9
                for y, x in zip(ys, xs):
                    ymin = max(y - 1, 0)
                    xmin = max(x - 1, 0)
                    ymax = min(y + 2, self.energylevels.shape[0])
                    xmax = min(x + 2, self.energylevels.shape[1])
                    self.energylevels[ymin:ymax, xmin:xmax] += 1
                    self.numflashes += 1
                ys, xs = np.where((self.energylevels > 9) * ~flashed)
            self.energylevels[self.energylevels > 9] = 0

    def iterate_until_simultaneous_flash(self):
        numiters = 0
        while np.any(self.energylevels > 0):
            self.iterate()
            numiters += 1
        return numiters

    @classmethod
    def parse_input(cls, fname: str):
        return cls(np.genfromtxt(fname, delimiter=1))


if __name__ == '__main__':
    octopi = DumboOctopi.parse_input('input.txt')
    octopi.iterate(100)
    print(octopi.numflashes)

    octopi = DumboOctopi.parse_input('input.txt')
    print(octopi.iterate_until_simultaneous_flash())
