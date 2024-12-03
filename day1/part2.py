from collections import Counter
from typing import List

from input_util import parse_two_columns


def solution(list1: List[int], list2: List[int]) -> int:
    counts = Counter(list2)
    return sum(num * counts.get(num, 0) for num in list1)


assert 31 == solution([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])

col1, col2 = parse_two_columns("input.txt")
print(solution(col1, col2))
