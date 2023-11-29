class Solution:
    def maxProduct(self, arr, n):
        maxi = None
        mini = None
        maxProduct = arr[0]
        for a in arr:
            if a < 0:
                temp = maxi
                if mini != None:
                    maxi = mini*a
                if temp != None:
                    mini = min(temp*a, a)
                else:
                    mini = a
            else:
                if a == 0:
                    maxi = 0
                    mini = 0
                    continue
                else:
                    if maxi == None:
                        maxi = a
                    else:
                        maxi = max(maxi*a,a)
                    if mini != None:
                            mini *= a
            if maxi != None and maxProduct < maxi:
                maxProduct = maxi
        return maxProduct
sol = Solution()
print(sol.maxProduct([3, -7, -9, 2, -7, 5, -4, -8], 8))

