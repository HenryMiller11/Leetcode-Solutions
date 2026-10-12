class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxi = float("-inf")

        while left < right:
            h = min(height[left], height[right])
            w = right - left

            maxi = max(maxi, h*w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxi