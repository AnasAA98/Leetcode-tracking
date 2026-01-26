class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col = len(board),len(board[0])
        def dfs(r,c):
            if r < 0 or r>=row or c<0 or c>=col or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)  
        # top row
        for i in range(col):
            if board[0][i] == 'O':
                dfs(0, i)

        # bottom row
        for j in range(col):
            if board[row-1][j] == 'O':
                dfs(row-1, j)

        # left col
        for k in range(row):
            if board[k][0] == 'O':
                dfs(k, 0)

        # right col
        for m in range(row):
            if board[m][col-1] == 'O':
                dfs(m, col-1)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == 'O':
                    board[r][c] ='X'

