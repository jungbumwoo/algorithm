from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest

from collections import defaultdict

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-101, next=head)
        ex_node = dummy
        
        current = head
        last_duplicated_value = None
        while current:
            # ex duplicate
            if current.val == last_duplicated_value:
                ex_node.next = current.next

            # new duplicate
            elif current.next and current.val == current.next.val:
                ex_node.next = current.next
                last_duplicated_value = current.val
            
            else:
                ex_node = current
            current = current.next
            
        
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
                input=Args(head = self.generate_input([1,2,3,3,4,4,5])),
                expect=[1,2,5]
            ),
            TestCase(
                name="test 2",
                input=Args(head = self.generate_input([1,1,1,2,3])),
                expect=[2,3]
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
