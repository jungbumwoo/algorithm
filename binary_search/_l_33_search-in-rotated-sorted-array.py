# https://leetcode.com/problems/search-in-rotated-sorted-array/

'''
counter example
nums = [1], target = 1
ans = 0
output = 1

if 등호 사용 잘못하였음
---------------------------------------

nums = [3, 5, 1], target = 3
ans = 0
output = -1

return type error

-------------------------------------

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
            if not left <= right:
                return False

            if nums[left] < nums[right]:
                return get_target(left, right, target)
                
            mid = (left + right) // 2

            if nums[left] < nums[mid]:
                temp = get_target(left, mid, target)
                if temp is not False:
                    return temp

            if nums[mid] < nums[right]:
                temp = get_target(right, mid, target)
                if temp is not False:
                    return temp

            if nums[mid] == target:
                return mid

            a = select(left, mid-1, target)
            if a is not False:
                return a
            b = select(mid +1, right, target)
            if b is not False:
                return b

            return False

        ans = select(0, len(nums)-1, target)
        if ans is False:
            return -1

        return ans
    

'''
다시 풀어봄.
재귀함수 쓰지 않고 풀이를 더 개선할 여지가 남았음.

다른 사람 풀이:
https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/14425/concise-o-log-n-binary-search-solution/

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(0, len(nums)-1, nums, target)
    
    def _search(self, left, right, nums, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1

        if nums[left] > nums[right]:
            mid = (left + right) // 2
            l = self._search(left=left, right=mid, nums=nums, target=target)
            r = self._search(left=mid+1, right=right, nums=nums, target=target)

            if l != -1:
                return l
            if r != -1:
                return r
            return -1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1