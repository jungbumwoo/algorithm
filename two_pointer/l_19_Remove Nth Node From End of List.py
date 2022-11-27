def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    nodes = head
    for _ in range(n):
        nodes = nodes.next
    
    if nodes is None:
        return head.next
        
    left_nodes = head
    while nodes:
        nodes = nodes.next
        if nodes is None:
            left_nodes.next = left_nodes.next.next
            return head
        
        left_nodes = left_nodes.next