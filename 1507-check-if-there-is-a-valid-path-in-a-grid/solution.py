class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        streets = {1:[(0,-1),(0,1)],
                   2:[(-1,0),(1,0)],
                   3:[(0,-1),(1,0)],  
                   4:[(1,0),(0,1)],
                   5:[(0,-1),(-1,0)],
                   6:[(-1,0),(0,1)],
                }
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            if r == row - 1 and c == col - 1:
                return True
            curr_st = grid[r][c]
            for dr, dc in streets[curr_st]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in visited:
                    next_st = grid[nr][nc]
                    if (-dr,-dc) in streets[next_st]: # can i go from current cell to next cell 
                        if dfs(nr,nc):
                            return True
            return False
        return dfs(0,0)





