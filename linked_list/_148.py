from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest

from collections import defaultdict

# fixme
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1*(10 ** 6))
        data = [(-1*(10 ** 6), dummy)]
        dummy.next = head

        while head:
            l, r = 0, len(data) - 1
            while l <= r:
                mid = (l + r) // 2
                current = data[mid][1]
                current_val = data[mid][0]
                print(f"l: {l}, r: {r}, mid:{mid}")

                if head.val > current_val and (current.next is None or head.val <= current.next.val):
                    next_ = head.next
                    head.next = current.next
                    # current.next = head

                    data_left = data[:mid+1]
                    data_right = data[mid+1:]
                    data_left.append((head.val, head))
                    data = data_left + data_right
                    
                    head = next_
                    break
                else:
                    r = mid - 1
            
        return self.convertOutput(dummy.next)
    
        
    def convertOutput(self, output):
        r = []
        while output:
            r.append(output.val)
            output = output.next
        return r

# Test
class TestSolution(unittest.TestCase):
    def generate_input(self, input):
        dummy = ListNode()
        ex_node = dummy

        for i in range(len(input)):
            node = ListNode(val=input[i])
            ex_node.next = node
            ex_node = node

        return dummy.next


    def test_solution(self):
        @dataclass
        class Args:
            head: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(head = self.generate_input([4,2,1,3])),
                expect=[1,2,5]
            ),
            TestCase(
                name="test 2",
                input=Args(head = self.generate_input([-1,5,3,4,0])),
                expect=[2,3]
            ),
            TestCase(
                name="test 2",
                input=Args(head = self.generate_input([])),
                expect=[]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(head=c.input.head)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )
        
        

if __name__ == '__main__':
    unittest.main()
