class Solution(object):
    def candy(self, ratings):
        arr = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] < ratings[i-1]:
                arr[i] = arr[i-1] - 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i],arr[i+1] - 1)
        return sum(arr)
sol = Solution()
print(sol.candy([1,2,2]))
