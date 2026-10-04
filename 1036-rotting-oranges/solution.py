class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        fresh_oranges = 0
        count_rotten = 0
        q = deque()
        # identify rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                # rotten row, rotten col
                rr, rc = q.popleft()
                dire = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in dire:
                    nr, nc = rr + dr, rc + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            fresh_oranges -= 1
                            grid[nr][nc] = 2
                            q.append((nr,nc))
            res += 1
        return res if fresh_oranges == 0 else -1 
