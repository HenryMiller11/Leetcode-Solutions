class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                sub = nums[start:start + k]

                # Check whether any cyclic rotation is sorted.
                drops = sum(
                    sub[i] > sub[(i + 1) % k]
                    for i in range(k)
                )

                if drops > 1:
                    valid = False
                    break

            if valid:
                # Rotations preserve each block's elements.
                # The sorted blocks must also be ordered globally.
                blocks = [
                    sorted(nums[i:i + k])
                    for i in range(0, n, k)
                ]

                for i in range(len(blocks) - 1):
                    if blocks[i][-1] > blocks[i + 1][0]:
                        valid = False
                        break

            if valid:
                ans += k

        return ans