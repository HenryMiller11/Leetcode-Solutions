class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        total = 0

        for i in nums:
            total += i - minimum

        return total