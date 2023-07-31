from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        candidates = {}

        for s in strs:
            counter = Counter(list(s))

            board = []
            for k, v in counter.items():
                board.append((k, v))
            
            board.sort()
            
            key = ""
            for element in board:
                key = key + element[0] + str(element[1])

            if key in candidates:
                candidates[key].append(s)
            else:
                candidates[key] = [s]
        output = []
        
        for _, value in candidates.items():
            output.append(value)
        return output