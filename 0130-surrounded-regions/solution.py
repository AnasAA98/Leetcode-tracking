class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find all the cells within the edges of the board and mark them and their adjcent cells O
        row, col = len(board), len(board[0])
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != "O":
                return
            board[r][c] = "P"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for i in range(row):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][col - 1] =="O":
                dfs(i,col - 1)
        for j in range(col):
            if board[0][j] == "O":
                dfs(0,j)
            if board[row - 1][j] == "O":
                dfs(row - 1, j)
        # now that the only O left are valid O's surrounded by X's
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"
        

