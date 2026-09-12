from typing import List
from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        arr.sort()

        starts = [x[0] for x in arr]

        # next index after choosing i
        nxt = [
            bisect_right(starts, arr[i][1])
            for i in range(n)
        ]

        # dp[i][k] = (maximum weight, lexicographically smallest indices)
        #
        # We only need k = 0..4.
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            idx = arr[i][3]
            weight = arr[i][2]

            for k in range(1, 5):

                # Option 1: skip interval i
                best_weight, best_indices = dp[i + 1][k]

                # Option 2: take interval i
                next_weight, next_indices = dp[nxt[i]][k - 1]

                take_weight = weight + next_weight
                take_indices = tuple(sorted((idx,) + next_indices))

                if take_weight > best_weight:
                    dp[i][k] = (take_weight, take_indices)

                elif take_weight < best_weight:
                    dp[i][k] = (best_weight, best_indices)

                else:
                    dp[i][k] = (
                        best_weight,
                        min(best_indices, take_indices)
                    )

        return list(dp[0][4][1])