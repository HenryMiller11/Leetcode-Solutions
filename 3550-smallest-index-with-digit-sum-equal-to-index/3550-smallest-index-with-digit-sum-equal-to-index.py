class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        for i in range(len(nums)):
            if digit_sum(nums[i]) == i:
                return i

        return -1