class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols= len(mat), len(mat[0])
        if not mat :
            return []
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                else:
                    mat[i][j] = math.inf
        if not q:
            return mat
        while q:
            directions =  [(1,0),(-1,0),(0,1),(0,-1)]
            r,c,dist = q.popleft()
            for dr,dc in directions:
                nr,nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if mat[nr][nc] == math.inf:
                        mat[nr][nc] = dist + 1
                        q.append((nr,nc,dist + 1))
        return mat
                    

                

        
