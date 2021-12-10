from typing import List


class SyntaxValidationException(Exception):
    pass


def validate_line(line: str) -> str:
    """Return invalid closing character if any is found, else return str of unclosed braces"""
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
    return ''.join(stack)


def score_syntax(lines: List[str]) -> int:
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137}
    return sum(score_map.get(validate_line(line), 0) for line in lines)


def score_incomplete_lines(lines: List[str]) -> int:
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    open_close_map = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    scores = []
    for line in lines:
        line_total = 0
        unclosed = validate_line(line)
        if unclosed in ')]}>':
            continue
        for chr in reversed(unclosed):
            line_total *= 5
            line_total += score_map[open_close_map[chr]]
        scores.append(line_total)
    scores.sort()
    return scores[int(len(scores) / 2)]


if __name__ == '__main__':
    print("Part 1")
    print(score_syntax([line.strip() for line in open('input.txt').readlines()]))
    print()
    print("Part 2")
    print(score_incomplete_lines([line.strip() for line in open('input.txt').readlines()]))
