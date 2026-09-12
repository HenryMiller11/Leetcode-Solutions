from typing import List


class SummaryRanges:

    def __init__(self):
        self.seen = [False] * 10001

    def addNum(self, value: int) -> None:
        self.seen[value] = True

    def getIntervals(self) -> List[List[int]]:
        ans = []
        i = 0

        while i <= 10000:
            if not self.seen[i]:
                i += 1
                continue

            start = i

            while i <= 10000 and self.seen[i]:
                i += 1

            ans.append([start, i - 1])

        return ans