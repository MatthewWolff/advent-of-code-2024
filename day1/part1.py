# https://adventofcode.com/2024/day/1
from typing import List

from input_util import parse_two_columns


def solution(list1: List[int], list2: List[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))


assert 11 == solution([3, 4, 3, 1, 3, 3], [4, 3, 5, 4, 9, 3])

col1, col2 = parse_two_columns("input.txt")
print(solution(col1, col2))
