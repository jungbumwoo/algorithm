from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        queue = deque()
        queue.append((root, 1))

        while queue:
            node, cnt = queue.popleft()

            if node.left is None and node.right is None:
                return cnt

            if node.left is not None:
                queue.append((node.left, cnt + 1))

            if node.right is not None:
                queue.append((node.right, cnt + 1))

        raise Exception('Not expected case Exists.')
    