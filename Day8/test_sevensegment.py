import unittest

from sevensegment import Decoder


class TestSevenSegmentSolver(unittest.TestCase):
    TEST_INPUT = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    TEST_CIPHER = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
    TEST_DIGITS = 'cdfeb fcadb cdfeb cdbaf'

    def test_solve_seven_segment(self):
        d = Decoder(self.TEST_CIPHER)

        self.assertEqual(d.decode('acedgfb'), 8)
        self.assertEqual(d.decode('cdfbe'), 5)
        self.assertEqual(d.decode('gcdfa'), 2)
        self.assertEqual(d.decode('fbcad'), 3)
        self.assertEqual(d.decode('dab'), 7)
        self.assertEqual(d.decode('cefabd'), 9)
        self.assertEqual(d.decode('cdfgeb'), 6)
        self.assertEqual(d.decode('eafb'), 4)
        self.assertEqual(d.decode('cagedb'), 0)
        self.assertEqual(d.decode('ab'), 1)

    def test_decode_and_solve(self):
        self.assertEqual(Decoder.decipher_and_decode_line(self.TEST_INPUT), 5353)


if __name__ == '__main__':
    unittest.main()
