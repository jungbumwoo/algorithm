class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def search(node, index):
            if node is None:
                return
            
            if index > len(result) - 1:
                result.append([node.val])
            else:
                result[index].append(node.val)

            search(node.left, index+1)
            search(node.right, index+1)
        search(root, 0)
        return result