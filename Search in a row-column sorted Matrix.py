# User function Template for python3

class Solution:

    # Function to search a given number in row-column sorted matrix.
    def search(self, matrix, n, m, x):
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] == x:
                return 1
            elif matrix[i][j] > x:
                j -= 1
            else:
                i += 1
        return 0