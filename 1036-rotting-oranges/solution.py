class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # step 1 find all rotten oranges and count number of fresh oranges
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_o = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_o += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        # early exit
        if fresh_o == 0:
            return 0
        if len(q) == 0:
            return -1

        # each level of the q represents time 1
        time = 0
        while q and fresh_o != 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                directions =  [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nr,nc = dr + r, dc + c
                    if 0<= nr < rows and 0<= nc < cols:
                        if grid[nr][nc] == 1:
                            fresh_o -=1
                            grid[nr][nc] = 2
                            q.append((nr,nc))
            time += 1
        return time if fresh_o == 0 else -1




        
