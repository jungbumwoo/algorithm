# math


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s = ''
        for i in range(len(digits)):
            s += str(digits[i])

        new_int = str(int(s) + 1)
        ans = []
        for j in range(len(new_int)):
            ans.append(int(new_int[j]))
        
        return ans
    
    # 좀 더 수학적으로 푼 풀이
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits.insert(0, 1)
        return digits