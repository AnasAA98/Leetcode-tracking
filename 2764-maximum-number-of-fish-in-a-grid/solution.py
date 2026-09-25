class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def explore(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            val = grid[r][c]
            grid[r][c] = 0
            return val + explore(r + 1, c) + explore(r - 1, c) + explore(r, c + 1) + explore(r, c - 1)
        
        res = 0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    res = max(res, explore(i,j))
        
        return res
