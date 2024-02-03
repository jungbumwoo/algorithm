# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# fixme 1.
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

# fixme 2.
# error case: [1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2]
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        data = {}
        ans = [0]

        def search(node, level, index):
            if node is None:
                return
            
            if level not in data:
                data[level] = index
            else:
                ans[0] = index - data[level] + 1
            
            search(node.left, level + 1, 2 * index - 1)
            search(node.right, level + 1, 2 * index)
        
        search(root, 0, 1)
        return ans[0]
    
# fixme 3. 
# error case: [1]
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        data = {}
        ans = [0]

        def search(node, level, index):
            if node is None:
                return
            
            if level not in data:
                data[level] = index
            else:
                ans[0] = max(ans[0], index - data[level] + 1)
            
            search(node.left, level + 1, 2 * index - 1)
            search(node.right, level + 1, 2 * index)
        
        search(root, 0, 1)
        print(data)
        return ans[0]

# solved            
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        data = {}
        ans = [0]

        def search(node, level, index):
            if node is None:
                return
            
            if level not in data:
                data[level] = index
                ans[0] = max(ans[0], 1)
            else:
                ans[0] = max(ans[0], index - data[level] + 1)
            
            search(node.left, level + 1, 2 * index - 1)
            search(node.right, level + 1, 2 * index)
        
        search(root, 0, 1)
        print(data)
        return ans[0]
            
                        