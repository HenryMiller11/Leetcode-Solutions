class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[x] += 1

            # Extend all subarrays ending at i - 1
            for r in range(k):
                if dp[r]:
                    nr = (r * x) % k
                    new_dp[nr] += dp[r]

            dp = new_dp

            # Every subarray ending here is one valid operation
            for r in range(k):
                ans[r] += dp[r]

        return ans