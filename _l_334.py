# fixme

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        stack.append((-1 * 2 ** 32))
        for n in nums:
            while stack[-1] >= n:
                stack.pop()

            stack.append(n)

            if len(stack) == 4:
                return True
        
        return False