class Solution(object):
    def minWindow(self, s, t):
        char = {}
        for i in range(len(t)):
            if t[i] in char:
                char[t[i]] += 1
            else:
                char[t[i]] = 1
        start = 0
        end = 0
        count = 0
        ans = s
        while end != len(s):
            if s[end] in char:
                if char[s[end]] > 0:
                    count += 1
                char[s[end]] -= 1
            if count == len(t):
                while start < end:
                    if s[start] in char:
                        if char[s[start]] < 0:
                            char[s[start]] += 1
                        else:
                            break
                    start += 1
                if end - start + 1 <= len(ans):
                    ans = s[start:end+1]
            end += 1
        for i in char:
            if char[i] > 0:
                return ""
        return ans

sol = Solution()
print(sol.minWindow("ADOBECODEBANC","ABC"))
