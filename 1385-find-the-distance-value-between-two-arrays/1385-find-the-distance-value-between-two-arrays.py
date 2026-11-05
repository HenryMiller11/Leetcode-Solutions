class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c = 0

        for i in range(len(arr1)):
            Flag = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    Flag = False
                    break

            if Flag:
                c += 1

        return c