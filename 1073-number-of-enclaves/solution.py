class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        seen = set()
        def dfs(r,c):
            if r<0 or r>= rows or c<0 or c>=cols or (r,c) in seen or grid[r][c] == 0:
                return
            seen.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols -1)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in seen:
                    count+=1
        return count


