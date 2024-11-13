# fixme
from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

'''
description
'''

class Solution:
    def solve(self, tokens: List[int]) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 
        def get_expression(stack):
            if len(stack) == 0:
                raise ValueError('unexpected')

            if stack[-1] not in {"+", "-", "/", "*"}:
                p = int(stack.pop())
                return p

            operator = stack.pop()
            right = get_expression(stack)
            left = get_expression(stack)

            if operator == "+":
                return int(right) + int(left)
            elif operator == "-":
                return int(left) - int(right)
            elif operator == "/":
                v = abs(int(left)) // abs(int(right))
                return v if int(left) * int(right) > 0 else -v
            elif operator == "*":
                return int(left) * int(right)
            else:
                raise ValueError('unexpected operator')
        
        return get_expression(tokens)
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            tokens: List[str]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]),
                expect=22
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(tokens=c.input.tokens)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
