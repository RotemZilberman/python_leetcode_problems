# User function Template for python3

class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        for i in range(n):
            flag = True
            for j in range(n):
                if M[i][j] == 1:
                    flag = False
                    break
            if flag:
                for k in range(n):
                    if k != i and M[k][i] == 0:
                        flag = False
                        break
            if flag:
                return True