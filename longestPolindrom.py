class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        maxStr = ""
        for i in range(len(s)):
            j = 0
            while(i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]):
                j += 1
            if maxLen < 2 * j - 1:
                maxLen = 2 * j - 1
                maxStr = s[i - j + 1:i + j]
            if i>0 and s[i] == s[i - 1]:
                j = 0
                while(i - j - 1 >= 0 and i + j < len(s) and s[i - j - 1] == s[i + j]):
                    j += 1
                if maxLen < 2 * j:
                    maxLen = 2 * j
                    maxStr = s[i - j:i + j]
        return maxStr

s = Solution()
print(s.longestPalindrome("babad"))
