import math
from sympy import *

class Solution:
    def findTwoElement( self,arr, n):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(n):
            sum1 += arr[i]
            sum2 += math.pow(arr[i], 2)
            sum3 +=i
        a = sum3 - sum1
        b = sum3 - sum2
        k, w = symbols('k w')
        expr1 = Eq(k - w - a, 0)
        expr2 = Eq(k**2 - 2*w**2 - b, 0)
        sol = solve((expr1, expr2), (k, w))
        print(sol)

sol = Solution()
sol.findTwoElement([1, 3, 3], 3)