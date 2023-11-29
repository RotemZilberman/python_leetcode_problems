class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        maxLen = 0
        usedChar = {}
        while end < len(s):
            if not (s[end] not in usedChar or usedChar[s[end]] < start):
                maxLen = max(maxLen, end - start)
                start = usedChar[s[end]] + 1
            usedChar[s[end]] = end
            end += 1
        return max(maxLen, end - start)

sul = Solution()

print(sul.lengthOfLongestSubstring("pwwkew"))
