
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Build suffix array
        sa = list(range(n))
        rank = nums[:]
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for i in range(1, n):
                a, b = sa[i - 1], sa[i]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )

                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build inverse suffix array
        pos = [0] * n

        for i, x in enumerate(sa):
            pos[x] = i

        # Calculate LCP array using Kasai's algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n:
                if nums[i + h] != nums[j + h]:
                    break
                h += 1

            lcp[r] = h

            if h:
                h -= 1

        # Find minimum unique subarray length
        ans = n

        for r in range(n):
            longest = lcp[r]

            if r + 1 < n:
                longest = max(longest, lcp[r + 1])

            remaining = n - sa[r]

            if longest < remaining:
                ans = min(ans, longest + 1)

        return ans
