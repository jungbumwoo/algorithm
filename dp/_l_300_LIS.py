import unittest

from dataclasses import dataclass
from functools import lru_cache
from typing import List, Optional, Tuple



# https://leetcode.com/problems/longest-increasing-subsequence/description/

'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
'''

class Solution:
    def solve(self, nums: List[int]) -> bool:
        # Time Complexity : O(n^2) 
        # Space Complexity : O(n)
        data = [1] * len(nums)
        ans = 1
        for i in range(len(nums)-1, -1, -1):
            maxi = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxi = max(maxi, data[j] + 1)
            data[i] = maxi 
            ans = max(data[i], ans)
        return ans


    # Memory Limit Exceeded -> lru_cache 라이브러리 안쓰고 직접 만들어쓰면 괜찮을 수도
    def solve1(self, nums: List[int]) -> bool:
        constraint_min = - (10 ** 4) - 1
        @lru_cache(maxsize=None)
        def select(i, before_picked):

            if i == len(nums):
                return 0

            current = nums[i]
            picked = constraint_min
            if current > before_picked:
                # picked
                picked = select(i+1, current) + 1

            # not picked
            not_picked = select(i+1, before_picked)

            return max(picked, not_picked)
        return select(0, constraint_min)

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [10,9,2,5,3,7,101,18]),
                expect=4,
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [0,1,0,3,2,3]),
                expect=4,
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [7,7,7,7,7,7,7]),
                expect=1
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()