class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Each node is:
        # [product of whole segment % k, counts of non-empty prefix products]
        #
        # cnt[p] = number of non-empty prefixes having product % k == p

        size = 1
        while size < n:
            size <<= 1

        prod = [1 % k] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        def make_leaf(value):
            value %= k
            c = [0] * k
            c[value] = 1
            return value, c

        # Build leaves
        for i in range(n):
            p, c = make_leaf(nums[i])
            prod[size + i] = p
            cnt[size + i] = c

        # Unused leaves are identity/empty segments.
        # We need a special merge for them, so track their length.
        length = [0] * (2 * size)
        for i in range(size):
            length[size + i] = 1 if i < n else 0

        for i in range(size - 1, 0, -1):
            length[i] = length[2 * i] + length[2 * i + 1]

        def merge(a, b):
            """
            Merge nodes a + b.

            a = (product_a, cnt_a, length_a)
            b = (product_b, cnt_b, length_b)
            """
            pa, ca, la = a
            pb, cb, lb = b

            if la == 0:
                return pb, cb[:], lb
            if lb == 0:
                return pa, ca[:], la

            p = (pa * pb) % k
            c = ca[:]

            # Prefixes that extend from A into B.
            for rem in range(k):
                c[(pa * rem) % k] += cb[rem]

            return p, c, la + lb

        def pull(i):
            left = (prod[2 * i], cnt[2 * i], length[2 * i])
            right = (prod[2 * i + 1], cnt[2 * i + 1], length[2 * i + 1])

            p, c, l = merge(left, right)
            prod[i] = p
            cnt[i] = c
            length[i] = l

        # Build tree
        for i in range(size - 1, 0, -1):
            pull(i)

        def update(pos, value):
            i = size + pos

            p, c = make_leaf(value)
            prod[i] = p
            cnt[i] = c
            length[i] = 1

            i >>= 1
            while i:
                pull(i)
                i >>= 1

        def query(left, right):
            """
            Query inclusive range [left, right].
            Returns (whole_product, prefix_counts, length).
            """
            left += size
            right += size + 1

            left_nodes = []
            right_nodes = []

            while left < right:
                if left & 1:
                    left_nodes.append(
                        (prod[left], cnt[left], length[left])
                    )
                    left += 1

                if right & 1:
                    right -= 1
                    right_nodes.append(
                        (prod[right], cnt[right], length[right])
                    )

                left >>= 1
                right >>= 1

            result = (1 % k, [0] * k, 0)

            for node in left_nodes:
                result = merge(result, node)

            for node in reversed(right_nodes):
                result = merge(result, node)

            return result

        ans = []

        for index, value, start, x in queries:
            # This update persists for all later queries.
            update(index, value)

            # Every possible remaining array is:
            # nums[start..start],
            # nums[start..start+1],
            # ...
            # nums[start..n-1]
            #
            # Therefore we need the number of prefixes whose
            # product % k == x.
            _, prefix_counts, _ = query(start, n - 1)

            ans.append(prefix_counts[x])

        return ans