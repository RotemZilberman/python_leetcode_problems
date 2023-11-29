class Solution:
    def checkTour(self, lis,n,startPoint):
        currentPetrol = 0
        MaxPetrol = 0
        Imax = 0
        Jmax = 0
        for i in range(n):
            if lis[i][0] == startPoint:
                currentPetrol = lis[i][1]
                MaxPetrol = currentPetrol
                Imax = i
                Jmax = i
                break