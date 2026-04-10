class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click 
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        row, col = len(board), len(board[0])
        def dfs (r,c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != "E":
                return
            count = 0
            dirs = [(1,0),(0,1),(-1,0),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)]
            for dr,dc in dirs:
                nr,nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == "M":
                    count +=1
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for dr,dc in dirs:
                    dfs(r + dr, c + dc)
        dfs(r,c)
        return board


