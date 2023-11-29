# User function Template for python3

class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        # code here
        ls = []
        i = 0
        j = 0
        while i < r and j < c:
            for k in range(j, c):
                ls.append(matrix[i][k])
            i += 1
            for k in range(i, r):
                ls.append(matrix[k][c - 1])
            c -= 1
            if i < r:
                for k in range(c - 1, j - 1, -1):
                    ls.append(matrix[r - 1][k])
                r -= 1
            if j < c:
                for k in range(r - 1, i - 1, -1):
                    ls.append(matrix[k][j])
                j += 1
        return ls
sol = Solution()
print(sol.spirallyTraverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3))