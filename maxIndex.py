#User function Template for python3
class Solution:
    def s(self, arr):
        ls = []
        for i in range(len(arr)):
            if i == 0:
                ls.append(arr[i])
            else:
                if arr[i] > ls[i-1]:
                    ls.append(arr[i])
                else:
                    ls.append(ls[i-1])
        return ls

    def maxIndexDiff(self,arr,n):
        arr = self.s(arr)
        fo