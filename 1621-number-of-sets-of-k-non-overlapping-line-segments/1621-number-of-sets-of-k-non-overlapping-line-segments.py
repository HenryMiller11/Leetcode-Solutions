class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j][i] = number of ways to draw j segments
        # using points 0..i
        dp = [[0] * n for _ in range(k + 1)]

        # 0 segments: exactly 1 way
        for i in range(n):
            dp[0][i] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(n):
                # dp[j-1][i-1] is the number of ways where
                # the new segment starts at some point <= i-1.
                if i > 0:
                    prefix = (prefix + dp[j - 1][i - 1]) % MOD

                # Either:
                # 1. don't end a segment at i
                # 2. end a new segment at i
                dp[j][i] = (dp[j][i - 1] if i > 0 else 0)
                dp[j][i] = (dp[j][i] + prefix) % MOD

        return dp[k][n - 1]