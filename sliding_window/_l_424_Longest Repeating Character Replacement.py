class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        inital_window_size = k + 1 # 바꾸는 수 (k) + 최소 하나 (1)

        l, r = 0, 0 + inital_window_size - 1
        
        data = {}
        max_exists = 0
        for i in range(l, r + 1):
            if s[i] not in data:
                data[s[i]] = 1
            else:
                data[s[i]] += 1
            
            max_exists = max(data[s[i]], max_exists)
        
        window_size = k + max_exists
        search_end_point = len(s) - window_size

        def search(index, size, k):
            temp = {}
            max_exists = 0
            for t in range(size):
                point = index + t

                if point >= len(s):
                    return max_exists + k

                if s[point] not in temp:
                    temp[s[point]] = 1
                else:
                    temp[s[point]] += 1

                max_exists = max(max_exists, temp[s[point]])
            
            return max_exists + k


        for i in range(0, search_end_point):
            new_window_size = search(i, window_size, k)
            while new_window_size > window_size:
                window_size = new_window_size
                new_window_size = search(i, window_size, k)
                
        return window_size