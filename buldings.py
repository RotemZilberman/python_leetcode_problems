class Solution:
    def getMinDiff(self, arr, n, k):
        max = arr[0]+k
        min = arr[0]+k
        for number in arr:
            if not((0 <= min <= number - k <= max) or (0 <= min <= number + k <= max)):
                if min - (number-k) > (number+k) - max:
                    max = number+k
                else:
                    min = number-k
        print(max, min)
        return max-min

sol = Solution()
print(sol.getMinDiff([1, 5, 8, 10], 4, 2))