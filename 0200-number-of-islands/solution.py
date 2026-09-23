class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] == "0":
                return
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    res += 1
        return res
        

