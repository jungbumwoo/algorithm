from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/minimum-size-subarray-sum

'''
target 과 일치되는 subarray 중 가장 짧은 길이를 return하기
'''

class Solution:
    def solve(self, target: int, nums: List[int]) -> int:
        # 이거 풀고 다른 풀이들도 봐보기.
        raise NotImplementedError

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            target: int
            nums: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(target=7, nums = [2,3,1,2,4,3]),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(target=4, nums = [1,4,4]),
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
