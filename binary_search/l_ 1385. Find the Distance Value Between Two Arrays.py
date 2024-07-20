class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1, arr2 = sorted(arr1), sorted(arr2)
        count = 0
        for i in range(len(arr1)):
            range_left, range_right = arr1[i] - d, arr1[i] + d
            if not self.is_exist(range_left, range_right, arr2):
                count += 1
        
        return count

    def is_exist(self, range_left, range_right, arr2):
        left, right = 0, len(arr2) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr2[mid] >= range_left and arr2[mid] <= range_right:
                return True
            elif arr2[mid] < range_left:
                left = mid + 1
            elif arr2[mid] > range_right:
                right = mid - 1
            else:
                raise ValueError('unexpected case')
        return False
