class Solution:

    def checkTour(self, lis,n,startPoint):
        current = startPoint
        count = 0
        for i in range(n):
            count += lis[current][0] - lis[current][1]
            if count < 0:
                return False
            current = (current + 1) % n
        return True

    def tour(self, lis, n):
        # Code here
        max = 0
        index = -1
        current = -1
        count = 0
        for i in range(n):
            if lis[i][0] - lis[i][1] >= 0:
                if current == -1:
                    current = i
                    count = 0
                count += lis[i][0] - lis[i][1]
                if i == n-1:
                    j = 0
                    while j < current:
                        if lis[j][0] - lis[j][1] < 0:
                            break
                        count += lis[j][0] - lis[j][1]
                        j += 1
                    if count > max:
                        max = count
                        index = current
            else:
                if count > max:
                    max = count
                    index = current
                current = -1
                count = 0
        if self.checkTour(lis,n,index):
            return index
        else:
            return -1
sol = Solution()
print("hi")
jwkwnjfvnkw
