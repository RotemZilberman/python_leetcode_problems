# User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def sum2(self, arr):
        sum2 = [[0 for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                sum2[i][j] = arr[i] + arr[j]
        return sum2
    def check(self, arr, target, i, j):
        k = j+1
        l = len(arr) - 1
        while k < l:
            if arr[k] + arr[l] == target:
                print(arr[i], arr[j], arr[k], arr[l])
                return True
            elif arr[k] + arr[l] > target:
                l -= 1
            else:
                k += 1
        return False

    def fourSum(self, arr, k):
        arr.sort()
        sum2 = self.sum2(arr)
        boll = False
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                target = k-arr[i]-arr[j]
                boll = self.check(arr, target, i, j)

        if boll is False:
            print(-1)

#check for 11 42 29 73 21 19 84 37 98 24 15 70 13 26 91 80 56 73 62 70 96 81 5 25 84 27 36 5 46 29 13 57 24 95 82 45 14 67 34 64 43 50 87 8} and 457
sol = Solution()
arr = [11, 42, 29, 73, 21, 19, 84, 37, 98, 24, 15, 70, 13, 26, 91, 80, 56, 73, 62, 70, 96, 81, 5, 25, 84, 27, 36, 5, 46, 29, 13, 57, 24, 95, 82, 45, 14, 67, 34, 64, 43, 50, 87, 8]
target = 456
sol.fourSum(arr, target)