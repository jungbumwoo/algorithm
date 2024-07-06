class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        sorted_num = sorted(nums)
        ans = 0
        for i in range(0, len(nums) -2):
            for j in range(i+1, len(nums) -1):
                ans += self.find(sorted_num[i] + sorted_num[j], sorted_num[j+1:])

        return ans

    def find(self, target, candidates):
        if len(candidates) == 0:
            return 0

        left, right = 0, len(candidates) - 1
        mid = None
        while left <= right:
            mid = (left + right) // 2

            if candidates[mid] <= target:
                right = mid - 1
            else:
                left = mid + 1

        return len(candidates) - mid