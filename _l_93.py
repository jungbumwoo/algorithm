from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/restore-ip-addresses/

'''
fix me 
'''

class Solution:
    def solve(self, s: str) -> List[str]:
        ans = []
        temp = []
        cache = set()
        def select(index, cnt):
            if index >= len(s):
                if len(temp) == 4:
                    ip = '.'.join(temp)
                    if ip not in cache:
                        cache.add(ip)
                        ans.append(ip)

                return 0

            if cnt >= 2 and s[index] == 0:
                return

            new = int(s[index:index+cnt])
            if new > 255:
                return
            
            temp.append(str(new))
            select(index+cnt, 1)
            temp.pop()

            temp.append(str(new))
            select(index+cnt, 2)
            temp.pop()

            temp.append(str(new))
            select(index+cnt, 3)
            temp.pop()

        select(0, 1)
        select(0, 2)
        select(0, 3)

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
                input=Args(s = "25525511135"),
                expect=["255.255.11.135","255.255.111.35"]
            ),
            TestCase(
                name="test 2",
                input=Args(s = "0000"),
                expect=["0.0.0.0"]
            ),
            TestCase(
                name="test 3",
                input=Args(s = "101023"),
                expect=["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
