import unittest
from textwrap import dedent

import diagnostic


class MyTestCase(unittest.TestCase):
    TEST_INPUT = dedent("""\
                00100
                11110
                10110
                10111
                10101
                01111
                00111
                11100
                10000
                11001
                00010
                01010""")

    TEST_INPUT_ARR = diagnostic.create_boolean_array(TEST_INPUT)

    def test_sample(self):
        self.assertEqual(diagnostic.calculate_gamma_rate(self.TEST_INPUT), 22)
        self.assertEqual(diagnostic.calculate_epsilon_rate(self.TEST_INPUT), 9)
        self.assertEqual(diagnostic.calculate_power_consumption(self.TEST_INPUT), 198)

    def test_get_frequency_dict(self):
        arr = diagnostic.create_boolean_array(self.TEST_INPUT)
        self.assertDictEqual(diagnostic.get_frequency_dict(arr, 0), {0: 5, 1: 7})
        self.assertDictEqual(diagnostic.get_frequency_dict(arr, 1), {0: 7, 1: 5})
        self.assertDictEqual(diagnostic.get_frequency_dict(arr, 2), {0: 4, 1: 8})
        self.assertDictEqual(diagnostic.get_frequency_dict(arr, 3), {0: 5, 1: 7})
        self.assertDictEqual(diagnostic.get_frequency_dict(arr, 4), {0: 7, 1: 5})

    def test_calculate_oxygen_generator_rating(self):
        self.assertEqual(diagnostic.calculate_oxygen_generator_rating(self.TEST_INPUT_ARR), 23)

    def test_calculate_c02_scrubber_rating(self):
        self.assertEqual(diagnostic.calculate_co2_scrubber_rating(self.TEST_INPUT_ARR), 10)

    def test_calculate_life_support_rating(self):
        self.assertEqual(diagnostic.calculate_life_support_rating(self.TEST_INPUT_ARR), 230)


if __name__ == '__main__':
    unittest.main()
