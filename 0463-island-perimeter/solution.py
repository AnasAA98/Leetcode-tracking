class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        per = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    per+=4
                    if j + 1 < n and grid[i][j+1] == 1:
                        per-=1
                    if i + 1 < m and grid[i+1][j] == 1:
                        per-=1
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        per-=1
                    if j -1 >= 0 and grid[i][j-1] ==1:
                        per-=1
        return per
