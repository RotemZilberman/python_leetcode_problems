#User function Template for python3
class Solution2:
    def helper(self, arr, n, i, sum1):
        if i == n:
            return abs(sum1)
        diff1 = self.helper(arr, n, i + 1, sum1 + arr[i])
        diff2 = self.helper(arr, n, i + 1, sum1 - arr[i])
        return min(diff1, diff2)

    def minDifference(self, arr, n):
        return self.helper(arr, n, 0, 0)



class Solution:
    def helper(self, arr, n, i, sum):
        if i == n:
            return abs(sum)
        a = self.helper(arr, n, i + 1, sum + arr[i])
        b = self.helper(arr, n, i + 1, sum - arr[i])
        return min(a, b)

    def minDifference(self, arr, n):
        total_sum = sum(arr)
        array_2d = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]

        # Initialize the base case
        for i in range(n + 1):
            array_2d[i][0] = True

        # Fill the dynamic programming table
        for i in range(1, n + 1):
            for j in range(total_sum + 1):
                array_2d[i][j] = array_2d[i - 1][j]
                if arr[i - 1] <= j:
                    array_2d[i][j] |= array_2d[i - 1][j - arr[i - 1]]

        # Find the minimum difference
        min_diff = float('inf')
        for j in range(total_sum // 2, -1, -1):
            if array_2d[n][j]:
                min_diff = total_sum - 2 * j
                break

        return min_diff


sol = Solution()
print(sol.minDifference([1, 6, 11, 5], 4))


