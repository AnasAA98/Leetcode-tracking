class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c,pr,pc):
            visited.add((r,c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= row or nc < 0 or nc >= col:
                    continue
                elif (nr,nc) == (pr,pc):
                    continue
                elif grid[nr][nc] != grid[r][c]:
                    continue
                elif (nr,nc) in visited:
                    return True
                elif dfs(nr, nc, r, c):
                    return True
            return False
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited:
                    if dfs(i,j,-1,-1):
                        return True
        return False
