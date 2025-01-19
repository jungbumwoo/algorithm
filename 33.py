class Solution:
    def search(self, nums: List[int], target: int) -> int:

        self.nums = nums
        return self.dfs(0, len(nums)-1, target)

    def dfs(self, left, right, target):

        if left == right:
            if self.nums[left] == target:
                return left
            return -1
        
        if self.nums[left] > self.nums[right]:
            mid = (left + right) // 2
            l = self.dfs(left, mid, target)
            if l != -1:
                return l

            return self.dfs(mid+1, right, target)
        
        while left <= right:
            mid = (left + right) // 2

            if self.nums[mid] == target:
                return mid

            if self.nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1