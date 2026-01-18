class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        mins = 0
        fresh_orange = 0
        # get number of all fresh oranges
        # get also position of all rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_orange += 1

        # bfs minute by minute

        while q and fresh_orange != 0:
            for _ in range(len(q)):
                current_row, curr_cols = q.popleft()

                neighbors = [
                    (current_row + 1, curr_cols),
                    (current_row - 1, curr_cols),
                    (current_row, curr_cols + 1),
                    (current_row, curr_cols - 1),
                ]
                for nei_r, nei_c in neighbors:
                    if 0<=nei_r<rows and 0 <= nei_c < cols:
                        if grid[nei_r][nei_c] == 1:
                            grid[nei_r][nei_c] = 2
                            fresh_orange-=1
                            q.append((nei_r,nei_c))
            mins+=1
        return mins if fresh_orange == 0 else -1

