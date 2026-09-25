class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Step 1: identify all the 0 on the edge of the board
        step 2: for 0 on the edge run DFS such that all connected cells to it are marked as visited 
        Step 3: the ones that are left unmarked need to mark them back to X
        """
        rows = len(board)
        cols = len(board[0])
        temp = []
        # 1st and last row 
        for j in range(cols):
            if board[0][j] == "O":
                temp.append((0,j))
            if board[rows - 1][j] == 'O':
                temp.append((rows - 1,j))
        # 1st and last col
        for i in range(rows):
            if board[i][0] == "O":
                temp.append((i,0))
            if board[i][cols - 1] == "O":
                temp.append((i, cols - 1))

        # DFS over the edges to mark the ones that should not be changed
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "Z"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # mark them now
        for dr, dc in temp:
            dfs(dr,dc)
        # replacing the temp value and the surrounded O's
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"
                
