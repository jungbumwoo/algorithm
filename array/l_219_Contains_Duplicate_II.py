class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in data:
                index = data[num]

                if i - index <= k:
                    return True

            data[num] = i
            
        return False
