class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_left, new_right = newInterval[0], newInterval[1]
        
        ans = []
        already_handled = False
        ing = [new_left, new_right]
        for i in range(len(intervals)):
            left, right = intervals[i][0], intervals[i][1]

            if ing[1] < left:
                if already_handled is False:
                    ans.append(ing)
                    already_handled = True
                ans.append([left, right])
            elif right < ing[0]:
                ans.append([left, right])
                continue
            elif already_handled is False and (ing[0] <= right or ing[1] >= left):
                ing[0] = min(left, ing[0])
                ing[1] = max(right, ing[1])
            else:
                raise

        if already_handled is False:
            ans.append(ing)
        
        return ans
