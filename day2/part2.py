# https://adventofcode.com/2024/day/2
from typing import List

from input_util import parse_matrix, parse_numbers_from_string
from part1 import is_valid as is_valid_og


def solution(matrix: List[List[int]]) -> int:
    return sum(map(is_valid, matrix))


def is_valid(lst: List[int], freebie_used=False) -> int:
    modifier = 1 if lst[1] < lst[0] else -1

    # check solution right away if ignoring first and last entries (avoid edge cases)
    if not freebie_used:
        if is_valid(lst[1:], True) or is_valid(lst[:-1], True):
            return 1

    prev = lst[0]
    for i, curr in enumerate(lst[1:], start=1):
        valid = 1 <= (prev - curr) * modifier <= 3
        if valid or not freebie_used:
            if not valid:
                # check if this entry or the last entry should be skipped (consider: [59, 62, 65, 64, 65])
                return is_valid(lst[0:i] + lst[i + 1:], True) or is_valid(lst[0:i - 1] + lst[i:], True)
            prev = curr
        else:
            return 0
    return 1


def solution_brute(matrix):
    summed = 0
    for line in matrix:
        summed += 1 if any(is_valid_og(line[:i] + line[i + 1:]) for i in range(len(line))) else 0
    print(summed)


print(solution(parse_numbers_from_string("""7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9""")))

print(solution(parse_matrix("input.txt")))
