class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        set1 = list(set(nums)) 
        if len(set1) < 3:
            return max(set1)
        set1.sort()

        for i in range(len(set1)):
            return set1[-3]