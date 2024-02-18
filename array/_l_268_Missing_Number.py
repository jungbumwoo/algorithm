class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)
        for i in range(len(nums)):
            self.arrange(nums, i)
        
        for j in range(len(nums)):
            if j != nums[j]:
                return j
        
        return len(nums)
    
    @staticmethod
    def arrange(nums, i):
        if i < len(nums) and nums[i] == i:
            return

        if i < len(nums) and nums[i] == len(nums):
            temp = nums[len(nums) - 1]
            nums[len(nums) -1] = nums[i]
            Solution.arrange(nums, temp)
        else:
            temp = nums[i]
            nums[i] = i
            Solution.arrange(nums, temp)

        