class Solution:
    def distinctSubseqII(self, s: str) -> int:
        end = [0] * 26
        total = 0
        MOD = 10**9 + 7

        for ch in s:
            idx = ord(ch) - 97
            newEnd = (total + 1) % MOD

            # Add newly formed subsequences and subtract duplicates
            total = (total + newEnd - end[idx]) % MOD

            # Update count of subsequences ending with this character
            end[idx] = newEnd

        return total