class NumArray:
    
    def __init__(self, nums: List[int]):
        self.total = []
        temp = 0
        for i in range(len(nums)):
            new = temp + nums[i]
            temp = new
            self.total.append(new)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.total[right]
        return self.total[right] - self.total[left-1]
        
