class Solution:
    def countCommas(self, n: int) -> int:
        c = 0
        for i in range(1000,n+1):
            if n >= 1000:
                c += 1
        return c