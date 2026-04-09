class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def explore(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            return 1 + explore(r + 1, c) + explore(r - 1, c) + explore(r, c + 1) + explore(r, c - 1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, explore(i,j))
        return res
