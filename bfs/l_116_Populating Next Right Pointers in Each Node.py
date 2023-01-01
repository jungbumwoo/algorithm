from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        queue.append(root)

        while queue:
            right_node = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node is not None:
                    node.next = right_node
                    right_node = node

                    queue.append(node.right)
                    queue.append(node.left)
        return root
