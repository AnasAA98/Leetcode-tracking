class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row, col= len(board), len(board[0])
        res = 0
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != 'X':
                return
            board[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    dfs(i,j)
                    res+=1
        return res
