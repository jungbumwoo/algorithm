class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        temp = []
        ans = []
        
        wordDict = set(wordDict)

        def select(i, temp, ans, wordDict):

            if i == len(s):
                ans.append(" ".join(temp[:]))
                temp = []
                return

            if i > len(s):
                print(f"unexpected case: temp: {temp}, i: {i}, s: {s}")
                raise ValueError

            for k in range(1, len(s)+1):
                if i + k > len(s):
                    continue

                w = s[i: i+k]
                if w not in wordDict:
                    continue
                else:
                    # print(f"w: {w}, i: {i}, i+k: {i+k}")
                    temp.append(w)    
                    select(i + k, temp, ans, wordDict)
                    temp.pop()
        
        select(0, temp, ans, wordDict)
        ans = set(ans)
        return list(ans)
            