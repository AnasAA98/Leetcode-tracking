class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        count = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                x,y = q.popleft()
                grid[x][y] = "2"
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dirs in directions:
                    curr_x,curr_y = dirs
                    curr_x+=x
                    curr_y+=y
                    if curr_x >=0 and curr_x<rows and curr_y>=0 and curr_y<cols and grid[curr_x][curr_y] == "1":
                        grid[curr_x][curr_y] = "2"
                        q.append((curr_x,curr_y))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count+=1

        return count
       
