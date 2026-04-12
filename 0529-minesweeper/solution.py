class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        i,j = click
        if board[i][j] == "M":
            board[i][j] = 'X'
            return board
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c]!="E":
                return
            count = 0 # count # of mines 
            dirs = [(-1,0),(1,0),(-1,-1),(0,-1),(1,-1),(-1,1),(0,1),(1,1)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "M":
                    count +=1
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)
        dfs(i,j)
        return board            
