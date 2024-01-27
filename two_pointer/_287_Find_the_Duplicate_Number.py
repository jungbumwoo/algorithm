# 기존 input을 변경하지 않고 다시 풀어보기

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            idx = abs(n)

            if nums[idx] < 0:
                return abs(n)
            
            nums[idx] = - nums[idx]
        