# https://leetcode.com/problems/daily-temperatures
# leetcode 739
# fixme 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        MAX_ABOVE = 10 ** 5
        if len(temperatures) == 1:
            return ans

        ex_index = [0]
        stack_top = [MAX_ABOVE]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if temp > stack_top[-1]:
                while temp > stack_top[-1]:
                    ans[ex_index[-1]] = i - ex_index[-1]
                    ex_index.pop()
                    stack_top.pop()
            ex_index.append(i)
            stack_top.append(temp)

        return ans
