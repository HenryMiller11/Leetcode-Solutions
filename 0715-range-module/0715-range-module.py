from bisect import bisect_left, bisect_right


class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        intervals = self.intervals

        i = bisect_left(intervals, [left, -1])

        # Merge with previous interval if it overlaps/touches.
        if i > 0 and intervals[i - 1][1] >= left:
            i -= 1

        new_left = left
        new_right = right

        j = i

        while j < len(intervals) and intervals[j][0] <= new_right:
            new_left = min(new_left, intervals[j][0])
            new_right = max(new_right, intervals[j][1])
            j += 1

        intervals[i:j] = [[new_left, new_right]]

    def queryRange(self, left: int, right: int) -> bool:
        intervals = self.intervals

        # Find the interval with the largest start <= left.
        i = bisect_right(intervals, [left, float('inf')]) - 1

        if i < 0:
            return False

        # [left, right) must be completely contained in it.
        return intervals[i][0] <= left and right <= intervals[i][1]

    def removeRange(self, left: int, right: int) -> None:
        intervals = self.intervals

        i = bisect_left(intervals, [left, -1])

        # The previous interval may overlap [left, right).
        if i > 0 and intervals[i - 1][1] > left:
            i -= 1

        j = i
        new_intervals = []

        while j < len(intervals) and intervals[j][0] < right:
            l, r = intervals[j]

            # Portion before [left, right)
            if l < left:
                new_intervals.append([l, left])

            # Portion after [left, right)
            if r > right:
                new_intervals.append([right, r])

            j += 1

        intervals[i:j] = new_intervals