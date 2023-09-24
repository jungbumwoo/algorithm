# https://leetcode.com/problems/search-in-rotated-sorted-array/

'''
counter example
nums = [1], target = 1
ans = 0
output = 1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        def get_target(left, right, target):

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False

        def select(left, right, target):
            # nums = [4,5,6,7,0,1,2], target = 3

            # l > r ? poissble?
            if not left < right:
                return False

            if nums[left] < nums[right]:
                return get_target(left, right, target)
                
            mid = (left + right) // 2

            if nums[left] < nums[mid]:
                temp = get_target(left, mid, target)
                if temp:
                    return temp

            if nums[mid] < nums[right]:
                temp = get_target(right, mid, target)
                if temp:
                    return temp

            if nums[mid] == target:
                return mid

            a = select(left, mid-1, target)
            if a:
                return a
            b = select(mid +1, right, target)
            if b:
                return b

            return False

        ans = select(0, len(nums)-1, target)
        if ans is False:
            return -1

        return ans
