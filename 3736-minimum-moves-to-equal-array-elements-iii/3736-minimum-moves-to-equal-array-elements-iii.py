class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = sum(nums)

        expected = max(nums) * len(nums)

        return expected - total