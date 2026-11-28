
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        min_price = min(p for f, p in items)
        max_factor = max(f for f, p in items)

        # Count frequency of each factor
        freq = [0] * (max_factor + 1)

        for f, p in items:
            freq[f] += 1

        # Count all divisible factors
        cnt = [0] * (max_factor + 1)

        for f in range(1, max_factor + 1):
            for j in range(f, max_factor + 1, f):
                cnt[f] += freq[j]

        # Collect profitable purchases
        deals = []

        for f, p in items:
            extra = cnt[f] - 1

            if extra > 0 and p <= 2 * min_price:
                deals.append((p, extra))

        # Cheapest double-reward purchases first
        deals.sort()

        ans = 0

        for price, extra in deals:
            take = min(extra, budget // price)

            ans += take * 2
            budget -= take * price

        # Spend remaining budget on cheapest single items
        ans += budget // min_price

        return ans
