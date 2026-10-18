from typing import List
from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left_ways = solve(left)
            right_ways = solve(right)

            ways = comb(len(left) + len(right), len(left))
            return (ways * left_ways * right_ways) % MOD

        return (solve(nums) - 1) % MOD