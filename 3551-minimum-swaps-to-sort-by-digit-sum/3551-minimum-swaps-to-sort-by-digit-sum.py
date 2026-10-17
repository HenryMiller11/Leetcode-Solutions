class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

        pos = {v: i for i, v in enumerate(nums)}
        ans = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]

                pos[nums[i]] = j
                pos[arr[i]] = i

                nums[i], nums[j] = nums[j], nums[i]
                ans += 1

        return ans