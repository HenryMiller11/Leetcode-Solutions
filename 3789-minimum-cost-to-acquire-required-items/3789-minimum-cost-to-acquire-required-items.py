
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        # Option 1: Buy separate items
        ans1 = need1 * cost1 + need2 * cost2

        # Option 2: Buy type 3 for common requirements
        common = min(need1, need2)

        ans2 = common * costBoth
        ans2 += (need1 - common) * cost1
        ans2 += (need2 - common) * cost2

        # Option 3: Buy only type 3 items
        ans3 = max(need1, need2) * costBoth

        return min(ans1, ans2, ans3)
