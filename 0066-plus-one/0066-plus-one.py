class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str1 = ''
        for i in range(len(digits)):
            str1 += str(digits[i])
        
        temp = int(str1) + 1
        str2 = str(temp)
        ans = []
        for i in range(len(str2)):
            ans.append(int(str2[i]))

        return ans

