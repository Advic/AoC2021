import unittest

from submarine import Submarine, AimingSubmarine


class SubmarineTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.submarine = Submarine()

    def test_parse_forward(self):
        self.submarine.parse("forward 3")
        self.assertEqual(3, self.submarine.position)  # add assertion here

    def test_parse_up(self):
        self.submarine.parse("up 2")
        self.assertEqual(-2, self.submarine.depth)  # add assertion here

    def test_parse_down(self):
        self.submarine.parse("down 1")
        self.assertEqual(1, self.submarine.depth)  # add assertion here

    def test_score(self):
        self.submarine.parse("forward 5")
        self.submarine.parse("down 3")
        self.assertEqual(15, self.submarine.score)

    def test_input(self):
        commands = ["forward 5",
                    "down 5",
                    "forward 8",
                    "up 3",
                    "down 8",
                    "forward 2"]
        for command in commands:
            self.submarine.parse(command)
        self.assertEqual(150, self.submarine.score)


class AimingSubmarineTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.submarine = AimingSubmarine()

    def test_input(self):
        commands = ["forward 5",
                    "down 5",
                    "forward 8",
                    "up 3",
                    "down 8",
                    "forward 2"]
        for command in commands:
            self.submarine.parse(command)
        self.assertEqual(900, self.submarine.score)


if __name__ == '__main__':
    unittest.main()
