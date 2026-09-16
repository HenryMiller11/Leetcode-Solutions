from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)

        for i, value in enumerate(arr):
            self.pos[value].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.pos[value]

        l = bisect_left(indices, left)
        r = bisect_right(indices, right)

        return r - l