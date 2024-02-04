class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode()

        dummy.next = head
        dummy.val = -1

        node = head
        before = dummy
        while node:
            if node.val == val:
                before.next = node.next
                # bofore = before
            else:
                before = node
            node = node.next
        
        return dummy.next