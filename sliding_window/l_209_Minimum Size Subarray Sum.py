from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
description
'''

class Solution:
    def solve(self, target: int, nums: List[int]) -> int:
        # Time Complexity :  
        # Space Complexity : 
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0

        total = [0] * (len(nums) + 1)
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            total[i+1] = t

        l, r = 0, 1
        ans = 10 ** 6
        while r < len(total):
            diff = total[r] - total[l]

            if diff >= target:
                ans = min(ans, r - l)
                l += 1
            else:
                r += 1

        if ans == 10 ** 6:
            return 0

        return ans

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]
            target: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(target = 7, nums = [2,3,1,2,4,3]),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(target = 4, nums = [1,4,4]),
                expect=1
            ),
            TestCase(
                name="test 3",
                input=Args(target = 11, nums = [1,1,1,1,1,1,1,1]),
                expect=0
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(target=c.input.target, nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()

