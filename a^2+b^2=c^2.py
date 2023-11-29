# User function Template for python3
class Solution:

    def checkTriplet(self, arr, n):
        arr.sort()
        for i in range(n - 1, -1, -1):
            m = arr[i] * arr[i]
            k = 0
            j = i - 1
            while k < j:
                if arr[k] * arr[k] + arr[j] * arr[j] == m:
                    print(arr[k],arr[j],arr[i])
                    print(arr)
                    return "Yes"
                elif arr[k] * arr[k] + arr[j] * arr[j] > m:
                    j -= 1
                else:
                    k += 1
        return "No"

sol = Solution()
print(sol.checkTriplet([4, 49, 1, 59, 19, 81, 97, 99, 82, 90, 99, 10, 58, 73, 23], 15))