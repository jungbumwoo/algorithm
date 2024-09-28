class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        r1 = []
        for element in set1:
            if element in set2:
                set2.remove(element)
            else:
                r1.append(element)

        r2 = [el for el in set2]

        return [r1, r2]
