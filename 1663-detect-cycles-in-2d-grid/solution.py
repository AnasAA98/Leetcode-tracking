class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        visited = set()
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        def dfs(r, c, pr, pc):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= row or nc < 0 or nc >= col:
                    continue
                if grid[nr][nc] != grid[r][c]:
                    continue
                if (nr, nc) == (pr, pc):
                    continue
                if (nr, nc) in visited:
                    return True
                if dfs(nr, nc, r, c):
                    return True
            return False
        for i in range(row):
            for j in range(col):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1):
                        return True
        return False
