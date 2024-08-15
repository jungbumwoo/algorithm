# https://leetcode.com/problems/daily-temperatures
# leetcode 739
# fixme 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        if len(temperatures) == 1:
            return ans

        ex_index = 0
        stack_top = 0
        for i in range(len(temperatures)):
            temp = temperatures[i]

            if temp > stack_top:
                while ex_index < i:
                    ans[ex_index] = i - ex_index
                    ex_index += 1
                
                stack_top = temp
                ex_index = i
        return ans
