class Solution(object):
    def CheckIfPalindrome(self,s,start,end,arrCheckIfPalindrome):
        if start > end:
            arrCheckIfPalindrome[start][end] = False
        if start == end:
            arrCheckIfPalindrome[start][end] = True
        if s[start] == s[end]:
            if arrCheckIfPalindrome[start+1][end-1] == None:
                self.CheckIfPalindrome(s, start+1, end-1, arrCheckIfPalindrome)
            arrCheckIfPalindrome[start][end] = arrCheckIfPalindrome[start+1][end-1]
        return False
    def minCut(self, s):
        arrCheckIfPalindrome = [[None for i in range(len(s))] for j in range(len(s))]

# 