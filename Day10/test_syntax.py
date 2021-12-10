import textwrap
import unittest

import syntax


class MyTestCase(unittest.TestCase):
    TEST_SYNTAX_LINES = textwrap.dedent("""\
        [({(<(())[]>[[{[]{<()<>>
        [(()[<>])]({[<{<<[]>>(
        {([(<{}[<>[]}>{[]{[(<()>
        (((({<>}<{<{<>}{[]{[]{}
        [[<[([]))<([[{}[[()]]]
        [{[{({}]{}}([{[{{{}}([]
        {<[[]]>}<{[{[{[]{()[[[]
        [<(<(<(<{}))><([]([]()
        <{([([[(<>()){}]>(<<{{
        <{([{{}}[<[[[<>{}]]]>[]]""")
    EXPECTED = ['', '', '}', '', ')', ']', '', ')', '>', '']

    def test_validate_lines(self):
        for expected, line in zip(self.EXPECTED, self.TEST_SYNTAX_LINES.split('\n')):
            self.assertEqual(expected, syntax.validate_line(line))

    def test_score_syntax(self):
        self.assertEqual(26397, syntax.score_syntax(self.TEST_SYNTAX_LINES.split('\n')))

    def test_score_incomplete_lines(self):
        self.assertEqual(288957, syntax.score_incomplete_lines(self.TEST_SYNTAX_LINES.split('\n')))


if __name__ == '__main__':
    unittest.main()
