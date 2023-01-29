from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/generate-parentheses/

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        workon = ['(']
        
        def handle(temp):
            length = len(temp)
            ans_length = n * 2
            lack = ans_length - length
            result = ''.join(temp) + ')' * lack
            ans.append(result)
            return 
        
        def work(l, r, n, temp):
            if r > l:
                return
            
            if l == n:
                handle(temp)
                return
            
            temp.append('(')
            work(l+1, r, n, temp)
            temp.pop()
            
            temp.append(')')
            work(l, r+1, n, temp)
            temp.pop()
            
        
        work(1, 0, n, workon)
        return ans

# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            n: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(n = 3),
                expect=["((()))","(()())","(())()","()(())","()()()"]
            ),
            TestCase(
                name="test 2",
                input=Args(n = 1),
                expect=["()"]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.generateParenthesis(n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
         