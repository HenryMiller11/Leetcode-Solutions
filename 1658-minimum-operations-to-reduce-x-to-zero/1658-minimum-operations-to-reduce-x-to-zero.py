from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # We need to remove everything if target == 0.
        if target == 0:
            return len(nums)

        # target < 0 means total sum is smaller than x.
        if target < 0:
            return -1

        left = 0
        curr = 0
        max_len = -1

        for right in range(len(nums)):
            curr += nums[right]

            # Shrink until window sum <= target.
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1

            if curr == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len