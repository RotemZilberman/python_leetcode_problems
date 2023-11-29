import random


class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        a = {}
        ls = int((n / 10))
        if n > 30:
            for i in range(ls):
                candidate = random.choice(nums)
                if a.__contains__(candidate):
                    a[candidate] += 1
                else:
                    a[candidate] = 1
            maxi = 0
            maxKey = 0
            for key in a.keys():
                if a[key] > maxi:
                    maxi = a[key]
                    maxKey = key
            return maxKey
        else:
            count = 0
            candidate = None

            for num in nums:
                if count == 0 or num == candidate:
                    count += 1
                    candidate = num
                else:
                    count -= 1

            return candidate

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))


