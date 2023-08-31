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