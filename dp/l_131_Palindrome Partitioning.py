from dataclasses import dataclass
from typing import List
import unittest


# https://leetcode.com/problems/palindrome-partitioning

'''
Given a string s, partition s such that every 
substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        temp = []

        def is_palindrome(sentence, s, e):
            checking_string = sentence[s:e]
            if len(checking_string) % 2 == 0:
                l, r = len(checking_string) // 2 - 1, len(checking_string) // 2
            else:
                l, r = len(checking_string) // 2, len(checking_string) // 2 

            while l >= 0:
                if checking_string[l] != checking_string[r]:
                    return False
                l -= 1
                r += 1
            return True

        def select(start):
            if start == len(s):
                ans.append(temp[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s, start, end):
                    temp.append(s[start:end])
                    select(end)
                    temp.pop()

        select(0)        
        return ans
        
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
                input=Args(s = "aab"),
                expect=[["a","a","b"],["aa","b"]]
            ),
            TestCase(
                name="test 2",
                input=Args(s = "a"),
                expect=[["a"]]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.partition(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
