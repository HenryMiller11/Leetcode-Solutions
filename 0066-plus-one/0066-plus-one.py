class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits)))
        num += 1

        return list(map(int, str(num)))

