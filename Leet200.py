grid = [["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]

#시간 초과
class MySolution:
    def numIslands(self, grid):
        self.grid = grid
        self.discovered = []

        self.m = len(grid)
        self.n = len(grid[0])

        number = 0

        for row in range(self.m) :
            for column in range(self.n):
                address = str(row) + " " + str(column)                    
                if (address not in self.discovered) and self.grid[row][column] == "1":


                    self.dfs(row, column)
                                        
                    number+=1
        return number
        

    def dfs(self, r, c):
        address = str(r) + " " +  str(c)
        if address not in self.discovered:
            self.discovered.append(address)
            print(self.discovered)
            if (r-1>=0) and self.grid[r-1][c]=="1":
                self.dfs(r-1, c)
            if (c+1<self.n) and self.grid[r][c+1]=="1":
                self.dfs(r, c+1)
            if (r+1<self.m) and self.grid[r+1][c]=="1":
                self.dfs(r+1, c)
            if (c-1>=0) and self.grid[r][c-1]=="1":
                self.dfs(r, c-1)
        return self.discovered


class Solution:
    def numIslands(self, grid):
        self.grid = grid
        cnt = 0
        self.m = len(grid)
        self.n = len(grid[0])

        for row in range(self.m):
            for col in range(self.n):
                if self.grid[row][col] == '1':
                    self.dfs(row, col)
                    cnt+=1
        return cnt
    
    def dfs(self, row, col):
        if row >= self.m or row < 0: return 
        elif col >= self.n or col < 0: return
        elif self.grid[row][col]!='1': return

        self.grid[row][col] = 'd'

        self.dfs(row-1, col)
        self.dfs(row+1, col)
        self.dfs(row, col-1)
        self.dfs(row, col+1)


s = Solution()
print(f'number of islands: {s.numIslands(grid)}')