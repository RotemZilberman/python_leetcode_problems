# User function Template for python3

class Solution:
    def rremove(self, S):
        i = 0
        length = len(S)
        while i < length - 1:
            j = i + 1
            flag = False
            while j < length - 1:
                if S[i] != S[j]:
                    break
                flag = True
                j += 1
            if flag:
                if j != length - 1:
                    S = S[:i] + S[i + j:]

                length = len(S)
                i = max(0, i - 1)
                continue
            i += 1
        return S


sol = Solution()
a = "accba"
print(sol.rremove(a))
