# input data 제대로 예상을 못해서 전혀 다르게 풀었다가 다시 풀게됨.
# 쉽게 풀 수 있는거 엉뚱하게 접근해서 어렵게 풀었었음.

import heapq

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        data = {}
        def search(node):
            if node is None:
                return
            
            search(node.left)
            search(node.right)

            if node.val not in data:
                data[node.val] = 1
            else:
                data[node.val] += 1

        search(root)
        l = []
        for k, v in data.items():
            l.append([v, k])
        
        l.sort(reverse=True)
        result = []
        last_value = -1
        for i in range(len(l)):
            v, k = l[i]
            if last_value == -1 or last_value == v:
                result.append(k)
                last_value = v
            else:
                break
        return result
            