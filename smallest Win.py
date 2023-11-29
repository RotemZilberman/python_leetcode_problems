class Solution:
    def smallestWindow(self, s, p):
        #code here
        map = {}
        for i in p:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        count = len(map)
        start = 0
        end = 0
        minLen = float('inf')
        minStart = 0
        while end < len(s):
            if s[end] in map:
                map[s[end]] -= 1
                if map[s[end]] == 0:
                    count -= 1
            while count == 0:
                if end - start + 1 < minLen:
                    minLen = (start, end)
                    minStart = start
                if s[start] in map:
                    map[s[start]] += 1
                    if map[s[start]] > 0:
                        count += 1
                start += 1
            end += 1
        if minLen == float('inf'):
            return -1
        return s[minStart:minStart+minLen]