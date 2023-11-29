class Solution:
    def permute(self, map, n, s, result):
        if n == 0:
            result.append(s)
        for key in map:
            if map[key] > 0:
                map[key] -= 1
                self.permute(map, n-1, s+key, result)
                map[key] += 1

    def find_permutation(self, S):
        map = {}
        for s in S:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        result = []
        self.permute(map, len(S), "", result)
        result.reverse()
        return result
sol = Solution()
print(sol.find_permutation("AAC"))


