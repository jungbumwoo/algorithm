# 한번에 풀었는데 다른 풀이 더 괜찮은게 있나 한번 찾아보기

class Solution:
    def frequencySort(self, s: str) -> str:
        dictionary = {}

        for word in s:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

        data = []
        for key, value in dictionary.items():
            data.append([value, key])
        
        data.sort(reverse=True)

        result = ""
        for i in range(len(data)):
            result += data[i][1] * data[i][0]
        return result