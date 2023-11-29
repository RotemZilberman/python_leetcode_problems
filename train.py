#User function Template for python3

class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        count = 0
        countMax = 0
        i = 0
        j = 0
        while j!=n:
            if i < n and arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                j += 1
                count -= 1
            if countMax < count:
                countMax = count
        return countMax
sol = Solution()
print(sol.minimumPlatform(6, [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))