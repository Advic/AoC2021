from typing import List


class SyntaxValidationException(Exception):
    pass


def validate_line(line: str) -> str:
    """Return invalid closing character if any is found"""
    stack = []
    close_open_map = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'}
    for chr in line:
        match chr:
            case '(' | '[' | '{' | '<':
                stack.append(chr)
            case ')' | ']' | '}' | '>':
                current_level = stack.pop()
                if current_level != close_open_map[chr]:
                    return chr
            case _:
                raise Exception(f"Invalid character %s detected" % chr)
    return ''


def score_syntax(lines: List[str]) -> int:
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        '': 0}
    return sum(score_map[validate_line(line)] for line in lines)


if __name__ == '__main__':
    print(score_syntax([line.strip() for line in open('input.txt').readlines()]))
