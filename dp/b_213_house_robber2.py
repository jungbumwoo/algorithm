from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/house-robber-ii/


class Solution:
    def solve(self, nums: List[int]) -> int:
        cache = {}
        if len(nums) == 1:
            return nums[0]

        def rob(i, robbed_yester, init):
            if (i, robbed_yester, init) in cache:
                return cache[(i, robbed_yester, init)]

            ans = 0
            if i == len(nums) -1:
                if robbed_yester is False and init is False:
                    return nums[i]
                return 0

            if robbed_yester:
                ans += rob(i+1, False, init)
            else:
                r = rob(i+1, True, init) + nums[i]
                not_r = rob(i+1, False, init)
                ans += max(r, not_r)

            cache[(i, robbed_yester, init)] = ans
            return ans

        return max(rob(1, False, False), rob(1, True, True) + nums[0])
        
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
                input=Args(nums = [2,3,2]),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [1,2,3,1]),
                expect=4
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
