class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Store minimum from i to the end
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        maxi = nums[0]

        for i in range(n):
            maxi = max(nums[i], maxi)

            mini = suffix_min[i]

            ans = maxi - mini

            if ans <= k:
                return i

        return -1