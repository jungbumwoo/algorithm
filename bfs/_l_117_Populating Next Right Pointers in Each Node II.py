# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        q = deque(list())
        q.append((root, 0))
        ex_handled = None
        ex_depth = -1

        while q:
            node, depth = q.popleft()
            if node is None:
                continue

            if ex_depth == depth:
                ex_handled.next = node

            ex_depth = depth
            ex_handled = node
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))

        return root