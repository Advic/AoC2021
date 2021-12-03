import unittest
from textwrap import dedent

import diagnostic


class MyTestCase(unittest.TestCase):

    def test_sample(self):
        diag_data = dedent("""\
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
        self.assertEqual(diagnostic.calculate_gamma_rate(diag_data), 22)
        self.assertEqual(diagnostic.calculate_epsilon_rate(diag_data), 9)
        self.assertEqual(diagnostic.calculate_power_consumption(diag_data), 198)


if __name__ == '__main__':
    unittest.main()
