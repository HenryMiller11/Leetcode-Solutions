from typing import List
class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        odd = [x for x in nums1 if x % 2 == 1]
        even = [x for x in nums1 if x % 2 == 0]

        if not odd or not even:
            return True

        min_odd = min(odd)
        min_even = min(even)

        # Make everything odd:
        # Every even x needs x - odd > 0.
        # The smallest odd is the easiest candidate to subtract.
        can_make_odd = all(x > min_odd for x in even)
        can_make_even = False

        return can_make_odd or can_make_even