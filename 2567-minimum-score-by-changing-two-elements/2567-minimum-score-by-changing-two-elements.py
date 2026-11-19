class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        ans = float('inf')

        for i in range(3):
            high = nums[n - 1 - i] - nums[2 - i]
            ans = min(ans, high)

        return ans