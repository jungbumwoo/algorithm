'''
시간 복잡도 개선 가능
'''

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        aliceSizes = sorted(aliceSizes)
        bobSizes = sorted(bobSizes)
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        for i in range(len(aliceSizes)):
            # target = bob_sum - (alice_sum - aliceSizes[i])
            # alice_sum - aliceSizes[i] + target = bob_sum + aliceSizes[i] - target
            target = (bob_sum - alice_sum + 2 * aliceSizes[i]) // 2
            left, right = 0, len(bobSizes) - 1

            while left <= right:
                mid = (left + right) // 2

                if bobSizes[mid] == target:
                    return [aliceSizes[i], target]
                elif bobSizes[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        raise ValueError('Unexpected case')

