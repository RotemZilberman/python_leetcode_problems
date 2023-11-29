class Solution:

    def validCheck(self,grid):
        rows = []
        for i in range(9):
            rows = [grid[i][j] for j in range(9)]
            rows.sort()
            for j in range(9):
                if rows[j] != j+1:
                    return False
        for i in range(9):
            rows = []
            for j in range(9):
                rows.append(grid[j][i])
            rows.sort()
            for j in range(9):
                if rows[j] != j+1:
                    return False
        return True

    def check(self,grid,row,num):
        if row == 8 and  num == 9:
            return self.validCheck(grid)
        if num == 9:
            return self.check(grid,row+1,0)
        if grid[row][num] != 0:
            return self.check(grid,row,num+1)
        for i in range(1,10):
            grid[row][num] = i
            if self.check(grid,row,num+1):
                return True
        grid[row][num] = 0
        return False


    def SolveSudoku(self,grid):
        status = self.check(grid,0,0)
        if status:
            return grid
        else:
            return -1

    def printGrid(self,arr):
        n = self.SolveSudoku(arr)
        if n == -1:
            print(-1)
            return
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=' ')
            print()

if __name__ == '__main__':
    sol = Solution()
    sol.printGrid([
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 0, 0, 0]
])


