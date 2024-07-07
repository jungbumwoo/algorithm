class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        for i in range(1, 101):

            left, right = 0, len(nums)-1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= i:
                    right = mid - 1
                else:
                    left = mid + 1

            if len(nums) - left == i:
                return i

        return -1