
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = [0] * 1501

        for f, p in items:
            freq[f] += 1

        groups = {}

        for f, p in items:
            if p > budget:
                continue

            value = 0

            for x in range(f, 1501, f):
                value += freq[x]

            groups.setdefault(p, []).append(value)

        neg = float('-inf')
        dp = [neg] * (budget + 1)
        dp[0] = 0

        ans = 0

        for p in sorted(groups, reverse=True):
            has = [neg] * (budget + 1)

            for value in groups[p]:
                for c in range(budget, p - 1, -1):
                    best = max(dp[c - p], has[c - p])

                    if best != neg:
                        has[c] = max(has[c], best + value)

                for c in range(budget, p - 1, -1):
                    if dp[c - p] != neg:
                        dp[c] = max(dp[c], dp[c - p] + value)

            for c in range(budget + 1):
                if has[c] != neg:
                    extra = (budget - c) // p
                    ans = max(ans, has[c] + extra)

        return ans
