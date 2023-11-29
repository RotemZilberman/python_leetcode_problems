class Solution(object):
    def intersectionSizeTwo(self, intervals):
        last1 = -1
        last2 = -1
        ans = 0
        intervals.sort(key=lambda x: x[1])
        for i in range(len(intervals)):
            if intervals[i][0] <= last2:
                # continue
            if intervals[i][0] <= last1:
                ans += 1
                if last1 == intervals[i][1]:
                    last2 = last1-1
                    continue
                else:
                    last2 = last1
                    last1 = intervals[i][1]
            else:
                ans += 2
                last2 = intervals[i][1] - 1
                last1 = intervals[i][1]
        return ans
sol = Solution()
print(sol.intersectionSizeTwo([[1,3],[3,7],[5,7],[7,8]]))