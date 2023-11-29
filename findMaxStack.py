from typing import List


class Solution:
    def maxEqualSum(self, N1: int, N2: int, N3: int, S1: List[int], S2: List[int], S3: List[int]) -> int:
        sum1 = sum(S1)
        sum2 = sum(S2)
        sum3 = sum(S3)
        i = 0
        j = 0
        k = 0
        while not (sum1 == sum2 == sum3):
            if i == len(S1) or j == len(S2) or k == len(S3):
                return 0
            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= S1[i]
                i += 1
            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= S2[j]
                j += 1
            elif sum3 >= sum1 and sum3 >= sum2:
                sum3 -= S3[k]
                k += 1
        return sum1


sol = Solution()
print(sol.maxEqualSum(3, 4, 2, [4, 2, 3], [1, 1, 2, 3], [1, 4]))
