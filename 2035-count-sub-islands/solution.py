class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])

        def explore(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return True
            if grid1[r][c] == 0:
                return False
            grid2[r][c] = 0
            valid = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                valid = explore(r + dr, c + dc) and valid

            return valid
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and explore(i, j):
                    res += 1
        return res 
