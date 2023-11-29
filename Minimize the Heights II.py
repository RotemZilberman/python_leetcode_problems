class Solution:
    def getMinDiff(self, arr, n, k):
        newArr = []
        d = 0
        for number in arr:
            newArr.append((number - k))
            newArr.append((d, number + k))
            d += 1
        newArr.sort(key=lambda x: x[1])
        i = 0
        j = len(newArr) - 1
        map = {i: 2 for i in range(n)}
        while i < j:
            if map[newArr[j][0]] > 1:
                map[newArr[j][0]] -= 1
                j -= 1
            elif map[newArr[i][0]] > 1:
                map[newArr[i][0]] -= 1
                i += 1
            else:
                break
        return newArr[j][1] - newArr[i][1]


sol = Solution()
# 2 6 3 4 7 2 10 3 2 1 and k=5
print(sol.getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 10, 5))
