class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            val = grid[r][c] 
            # mark as visited
            grid[r][c] = 0
            return val+dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    temp = dfs(i, j)
                    if temp % k == 0:
                        res += 1
        return res

