class Solution :
    def rearrangeString(self, str):
        map = [0 for i in range(26)]
        for char in str:
            map[ord(char)-ord('a')] += 1
        for i in range(26):
            if map[i] > len(str)/2:
                return 0
        return 1
sol = Solution()
print(sol.rearrangeString("aaabc"))