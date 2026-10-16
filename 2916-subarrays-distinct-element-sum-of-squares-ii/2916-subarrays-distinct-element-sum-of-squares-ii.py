from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, l, r):
            if lazy[node] == 0:
                return

            v = lazy[node]
            length = r - l + 1

            sq[node] = (sq[node] + 2 * v * tree[node]
                        + v * v * length) % MOD
            tree[node] = (tree[node] + v * length) % MOD

            if l != r:
                lazy[node * 2] += v
                lazy[node * 2 + 1] += v

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            push(node, l, r)

            if qr < l or r < ql:
                return

            if ql <= l and r <= qr:
                v = 1
                length = r - l + 1

                sq[node] = (sq[node] + 2 * tree[node]
                            + length) % MOD
                tree[node] = (tree[node] + length) % MOD

                if l != r:
                    lazy[node * 2] += v
                    lazy[node * 2 + 1] += v

                return

            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans