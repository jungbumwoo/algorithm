# timeout

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1*(10 ** 6))

        while head:
            current = dummy
            while current:
                if head.val >= current.val and (current.next is None or head.val <= current.next.val):
                    next_ = head.next
                    head.next = current.next
                    current.next = head
                    
                    head = next_
                    break
                    
                current = current.next
        
        return dummy.next
