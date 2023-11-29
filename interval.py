class Solution:
    def overlappedInterval(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        maxi = intervals[0][1]
        min = intervals[0][0]
        for i in range(len(intervals)):
            if intervals[i][0] <= maxi:
                maxi = max(intervals[i][1], maxi)

            else:
                result.append([min, maxi])
                min = intervals[i][0]
                maxi = intervals[i][1]
        result.append([min, maxi])
        return result

sol = Solution()
print(sol.overlappedInterval([[1,3],[2,4],[6,8],[9,10]]))

