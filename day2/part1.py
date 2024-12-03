# https://adventofcode.com/2024/day/2
from typing import List

from input_util import parse_matrix, parse_numbers_from_string


def solution(matrix: List[List[int]]) -> int:
    return sum(map(is_valid, matrix))


def is_valid(lst: List[int]) -> int:
    prev = lst[0]
    modifier = 1 if lst[1] < lst[0] else -1

    for curr in lst[1:]:
        if 1 <= (prev - curr) * modifier <= 3:
            prev = curr
        else:
            return 0

    return 1


print(solution(parse_numbers_from_string("""7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9""")))

print(solution(parse_matrix("input.txt")))
