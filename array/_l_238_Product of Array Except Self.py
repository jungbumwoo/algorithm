class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)

        pre = 1
        for i in range(len(nums)):
            pre *= nums[i]
            prefix.append(pre)

        suff = 1
        for j in range(len(nums)-1, -1, -1):
            suff *= nums[j]
            suffix[j] = suff

        ans = [0] * len(nums)
        ans[0] = suffix[1]
        ans[-1] = prefix[-2]

        for k in range(1, len(nums)-1):
            ans[k] = prefix[k-1] * suffix[k+1]
        return ans