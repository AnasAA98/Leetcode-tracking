class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j,0)) # row,col,dist
                else:
                    mat[i][j] = -1
        while q:
            r, c, dist = q.popleft()
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] == -1:
                    mat[nr][nc] = dist + 1
                    q.append((nr, nc, dist +1))
        return mat
