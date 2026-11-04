
from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        arr = [bisect_left(vals, v) + 1 for v in nums]

        # Fenwick Trees
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(bit, i, val):
            while i <= m:
                bit[i] += val
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(kth):
            idx = 0
            bit_mask = 1 << (m.bit_length() - 1)

            while bit_mask:
                nxt = idx + bit_mask

                if nxt <= m and cnt[nxt] < kth:
                    idx = nxt
                    kth -= cnt[nxt]

                bit_mask >>= 1

            return idx + 1

        def get_cost():
            mid_idx = kth((x + 1) // 2)
            median = vals[mid_idx - 1]

            left_count = query(cnt, mid_idx)
            left_sum = query(sm, mid_idx)

            total_sum = query(sm, m)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        # Calculate cost of every window
        cost = []

        for i in range(n):
            update(cnt, arr[i], 1)
            update(sm, arr[i], nums[i])

            if i >= x:
                update(cnt, arr[i - x], -1)
                update(sm, arr[i - x], -nums[i - x])

            if i >= x - 1:
                cost.append(get_cost())

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Take the last x elements
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + cost[i - x]
                    )

            prev = curr

        return prev[n]
