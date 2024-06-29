# input data 제대로 예상을 못해서 전혀 다르게 풀었다가 다시 풀게됨.
# 쉽게 풀 수 있는거 엉뚱하게 접근해서 어렵게 풀었었음.

import heapq

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        most_count = [0]
        data = {}

        def search(node, data):
            if node is None:
                return
            
            if node.val not in data:
                data[node.val] = 0
            data[node.val] += 1
            most_count[0] = max(most_count[0], data[node.val])

            search(node.left, data)
            search(node.right, data)
        
        search(root, data)
        result = []
        for k, v in data.items():
            if v == most_count[0]:
                result.append(k)
        return result

            