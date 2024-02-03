# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        data = {}
        ans = 0

        def search(node, level, index):
            global ans

            if node is None:
                return
            
            if level not in data:
                data[level] = index
            else:
                ans = index - data[level] + 1
            
            search(node.left, level + 1, 2 * index - 1)
            search(node.right, level + 1, 2 * index)
        
        search(root, 0, 1)
        return ans
            