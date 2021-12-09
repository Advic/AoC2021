import numpy as np


class SmokeBasin:
    def __init__(self, heightmap: np.array):
        self.heightmap = heightmap

    @classmethod
    def parse_input(cls, fname: str):
        return cls(np.genfromtxt(fname, delimiter=1))

    def identify_low_points(self):
        padded_heightmap = np.pad(self.heightmap, 1, constant_values=10)
        return np.where((self.heightmap < padded_heightmap[2:, 1:-1]) &
                        (self.heightmap < padded_heightmap[:-2, 1:-1]) &
                        (self.heightmap < padded_heightmap[1:-1, 2:]) &
                        (self.heightmap < padded_heightmap[1:-1, :-2]))

    def sum_risk_levels(self):
        return (self.heightmap[self.identify_low_points()] + 1).sum()

    def segment_basins(self):
        segment_image = -1 * np.ones(self.heightmap.shape, dtype=int)
        segment_image[np.where(self.heightmap == 9)] = 0
        for i, (x, y) in enumerate(list(zip(*self.identify_low_points())), 1):
            segment_image = self.floodfill(segment_image, x, y, i)
        return segment_image

    def find_largest_basins(self):
        basins = self.segment_basins()
        basin_sizes = np.array(list(enumerate(np.bincount(basins.ravel())))[1:])
        return basin_sizes[basin_sizes[:, 1].argsort()[::-1]][:3]

    def multiply_three_largest_basins(self):
        basin_product = 1
        for basin_num, basin_count in self.find_largest_basins()[:3]:
            basin_product *= basin_count
        return basin_product

    @staticmethod
    def floodfill(image, y, x, fillvalue, startvalue=None):
        if startvalue is None:
            startvalue = image[y, x]
        if image[y, x] != startvalue:
            return image

        image[y, x] = fillvalue
        if x > 0:
            image = SmokeBasin.floodfill(image, y, x - 1, fillvalue, startvalue)
        if x < image.shape[1] - 1:
            image = SmokeBasin.floodfill(image, y, x + 1, fillvalue, startvalue)
        if y > 0:
            image = SmokeBasin.floodfill(image, y - 1, x, fillvalue, startvalue)
        if y < image.shape[0] - 1:
            image = SmokeBasin.floodfill(image, y + 1, x, fillvalue, startvalue)
        return image


if __name__ == '__main__':
    print(SmokeBasin.parse_input('input.txt').sum_risk_levels())
    print(SmokeBasin.parse_input('input.txt').multiply_three_largest_basins())
