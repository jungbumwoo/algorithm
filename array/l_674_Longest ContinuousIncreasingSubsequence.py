# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        cnt = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
        return ans
