import random
from itertools import permutations

# Fisher-Yates Algorithm
# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

# Memory Limit Exceeded
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.permutation = list(permutations(self.nums, len(nums)))

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        rand_index = random.randrange(0, len(self.nums)-1)
        return self.permutation[rand_index]
    
# Timeout
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

        self._picked_cnt = 0
        self._picked = [False] * len(self.nums)
        self._shuffled = []

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        new_shuffled = self._shuffle()[:]
        self._picked_cnt = 0
        self._picked = [False] * len(self.nums)
        self._shuffled = []
        return new_shuffled

    def _shuffle(self):       
        while self._picked_cnt <= len(self.nums):
            while True:
                rand_index = random.randrange(0, len(self.nums) -1)
                if self._picked[rand_index]:
                    continue
            
            self._suffled.append(nums[rand_index])
            self._picked_cnt += 1
            self._picked[rand_index] = True

        