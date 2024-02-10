# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        
        dummy = ListNode()
        dummy.next = head

        self.head = dummy
        self.max_length = None
    
    def _get_random_value(self):
        if self.max_length:
            return random.randrange(1, self.max_length)
        return random.randrange(1, 10 ** 4)

    def getRandom(self) -> int:
        random_int = self._get_random_value()
        node = self.head
        length = 0

        while random_int:
            random_int -= 1
            length += 1

            if node.next is None:
                self.max_length = length
                return self.getRandom()

            node = node.next
        
        return node.val
