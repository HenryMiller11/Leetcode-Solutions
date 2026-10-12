class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        total = 0
        for i in nums:
            total += i

        return expected_sum - total