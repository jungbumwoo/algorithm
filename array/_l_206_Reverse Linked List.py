# Timeout..

import copy
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# timeout solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        ans, before = None, None
        node = head

        while node is not None:
            before = ans
            ans = copy.deepcopy(node)
            ans.next = before

            node = node.next

        return ans

        