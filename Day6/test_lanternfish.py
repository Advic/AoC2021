import unittest

from lanternfish import LanternFishSchool, EfficientLanternFishSchool


class TestLanternFishSchool(unittest.TestCase):
    INITIAL_STATE = '3,4,3,1,2'

    def test_eighteen_days(self):
        school = LanternFishSchool.parse_state(self.INITIAL_STATE)
        for i in range(18):
            school.simulate()

        self.assertEqual(school.count(), 26)

    def test_eighty_days(self):
        school = LanternFishSchool.parse_state(self.INITIAL_STATE)
        for i in range(80):
            school.simulate()

        self.assertEqual(school.count(), 5934)


class TestEfficientLanternFishSchool(unittest.TestCase):
    INITIAL_STATE = '3,4,3,1,2'

    def test_eighteen_days(self):
        school = EfficientLanternFishSchool.parse_state(self.INITIAL_STATE)
        for i in range(18):
            school.simulate()

        self.assertEqual(school.count(), 26)

    def test_eighty_days(self):
        school = EfficientLanternFishSchool.parse_state(self.INITIAL_STATE)
        for i in range(80):
            school.simulate()

        self.assertEqual(school.count(), 5934)


if __name__ == '__main__':
    unittest.main()
