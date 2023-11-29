count = 0

class Solution:

    def minSwaps(self, nums):
        global count
        copy = nums.copy()
        copy = [(copy[i], i) for i in range(len(copy))]
        copy.sort(key=lambda x: x[0])
        for i in range(len(nums)):
            if copy[i][0] != nums[i]:
                nums[i], nums[copy[i][1]] = nums[copy[i][1]], nums[i]
                count += 1
        return count
# Code here
sol = Solution()
print(sol.minSwaps([2 ,8, 5, 4]))