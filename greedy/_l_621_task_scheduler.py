from dataclasses import dataclass
from typing import List, Optional, Tuple

import heapq
import unittest



#  https://leetcode.com/problems/task-scheduler/

'''
description
'''

class Solution:
    def solve(self, tasks: List[str], n: int) -> int:
        # Time Complexity :  
        # Space Complexity : 

        raw = {}
        for i in range(len(tasks)):
            if tasks[i] in raw:
                raw[tasks[i]] += 1
            else:
                raw[tasks[i]] = 1

        # print(raw)

        queue = []
        heapq.heapify(queue)        

        for k, v in raw.items():
            heapq.heappush(queue, [-v, k])

        empty = 0
        cnt = 0
        while queue:
            # print(queue)
            temp = []
            empty = 0
        
            for _ in range(n+1):
                cnt += 1
                try:
                    v, k = heapq.heappop(queue)
                    v = -1 * v
                    v -= 1

                    if v:
                        temp.append([-v, k])
                except:
                    empty += 1
                    continue
        
            for q in range(len(temp)):
                heapq.heappush(queue, [temp[q][0], temp[q][1]])

        return cnt - empty

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            tasks: List[int]
            n: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(tasks = ["A","A","A","B","B","B"], n=2),
                expect=8
            ),
            TestCase(
                name="test 2",
                input=Args(tasks = ["A","A","A","B","B","B"], n=0),
                expect=6
            ),
            TestCase(
                name="test 3",
                input=Args(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n=2),
                expect=16
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(tasks=c.input.tasks, n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()


import heapq

class Solution:
    def solve(self, tasks: List[str], n: int) -> int:
        # 1
        raw = {}
        for i in range(len(tasks)):
            if tasks[i] in raw:
                raw[tasks[i]] += 1
            else:
                raw[tasks[i]] = 1

        queue = []
        heapq.heapify(queue)        

        for k, v in raw.items():
            heapq.heappush(queue, [v, k])

        empty = 0
        cnt = 0
        while queue:
            temp = []
            empty = 0
            for _ in range(n+1):
                cnt += 1
                try:
                    v, k = queue.heappop()

                    v -= 1

                    if v:
                        temp.append([v, k])
                except:
                    empty += 1
                    continue

            for q in range(len(temp)):
                heapq.heappush(queue, [temp[q][0], temp[q][1]])

        return cnt - empty