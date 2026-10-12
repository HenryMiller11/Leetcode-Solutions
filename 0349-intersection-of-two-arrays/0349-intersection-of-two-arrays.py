class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = list(set(nums1))
        set2 = list(set(nums2))
        ans = []
        for i in range(len(set1)):
            for j in range(len(set2)):
                if set1[i] == set2[j]:
                    ans.append(set1[i])
        return ans