class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = whether s[l..r] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length <= 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        # dp[i] = maximum number of valid palindromes
        # in s[0:i]
        dp = [0] * (n + 1)

        for r in range(n):
            # Don't use a palindrome ending at r
            dp[r + 1] = dp[r]

            # Try every palindrome ending at r
            for l in range(r + 1):
                if r - l + 1 >= k and pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]