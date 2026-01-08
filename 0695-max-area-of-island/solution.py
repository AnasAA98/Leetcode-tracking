class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def explore(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 or (r, c) in visited:
                return 0
            visited.add((r,c))
            return 1 + explore(r + 1, c ) + explore(r - 1, c )+ explore(r, c + 1)+ explore(r, c - 1)

        maxSzie = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr = explore(i, j)
                    maxSzie = max(curr, maxSzie)
        return maxSzie

