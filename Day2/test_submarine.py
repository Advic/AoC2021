import unittest

from submarine import Submarine


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.submarine = Submarine()

    def test_parse_forward(self):
        self.submarine.parse("forward 3")
        self.assertEqual(3, self.submarine.x)  # add assertion here

    def test_parse_up(self):
        self.submarine.parse("up 2")
        self.assertEqual(2, self.submarine.y)  # add assertion here

    def test_parse_down(self):
        self.submarine.parse("down 1")
        self.assertEqual(-1, self.submarine.y)  # add assertion here

    def test_score(self):
        self.submarine.parse("forward 5")
        self.submarine.parse("down 3")
        self.assertEqual(15, self.submarine.score)


if __name__ == '__main__':
    unittest.main()
