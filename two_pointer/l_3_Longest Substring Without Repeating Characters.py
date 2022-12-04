from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def solve(self, s: str) -> int:
        # Time Complexity :  O(n)
        # Space Complexity : O(n)
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 0
        data = set()
        answer = 0
        
        for l in range(len(s)):
            if s[l] not in data:
                data.add(s[l])
            else:
                answer = max(l - r, answer)
                
                while s[l] in data:
                    data.remove(s[r])
                    r += 1
                data.add(s[l])
        
        answer = max(l - r + 1, answer)
        return answer

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s = "abcabcbb"),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(s = "bbbbb"),
                expect=1
            ),
            TestCase(
                name="test 3",
                input=Args(s = "pwwkew"),
                expect=3
            ),
        ]

        
        for c in cases:
            solution = Solution()
            actual = solution.solve(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
