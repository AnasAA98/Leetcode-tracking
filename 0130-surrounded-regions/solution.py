class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] !="O":
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)        
        
        
        # need to add all the '0' on the edges to the dfs function
        
        # 1st and last row check
        for i in range(cols):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[rows-1][i] == 'O':
                dfs(rows-1, i)
        # left and right cols
        for j in range(rows):
            if board[j][0] == 'O':
                dfs(j,0)
            if board[j][cols-1] == 'O':
                dfs(j,cols-1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
