class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c>= cols or (r,c) in visited or grid[r][c]== 1:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        # top and bottom rows
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0,c)
            if grid[rows-1][c] == 0:
                dfs(rows-1,c)
        # left and right col
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r,0)
            if grid[r][cols-1] == 0:
                dfs(r,cols-1)
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i,j) not in visited:
                    result+=1
                    dfs(i,j)
        return result
