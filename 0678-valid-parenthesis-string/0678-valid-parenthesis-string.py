class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # Too many ')' even in the best case
            if high < 0:
                return False

            # low cannot be negative
            low = max(low, 0)

        return low == 0