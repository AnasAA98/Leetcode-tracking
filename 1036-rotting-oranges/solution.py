class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        q = deque()
        mins = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges+=1
        while q and fresh_oranges != 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                directions =  [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_oranges-=1
                            q.append((nr,nc))
            mins+=1
        return mins if fresh_oranges == 0 else -1
