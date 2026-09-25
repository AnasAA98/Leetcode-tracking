class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        
        res = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == '.':
                return
            board[r][c] = '.'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range (cols):
                if board[i][j] == 'X':
                    res += 1
                    dfs(i, j)
        
        return res
