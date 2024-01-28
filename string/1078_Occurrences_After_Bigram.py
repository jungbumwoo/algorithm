class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        text = list(text.split(" "))

        if len(text) < 3:
            return []

        f, s = 0, 1
        ans = []
        while s <= len(text) - 2:
            if text[f] == first and text[s] == second:
                ans.append(text[s + 1])
            
            f += 1
            s += 1
        
        return ans
