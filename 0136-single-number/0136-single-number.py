class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = defaultdict(int)

        for i in range(len(nums)):
            freq[nums[i]] += 1

        for n,c in freq.items():
            if c == 1:
                return n