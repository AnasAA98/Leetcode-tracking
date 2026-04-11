class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board),len(board[0])
        visited = set()
        def dfs(r,c,index):
            if r < 0 or r>= row or c < 0 or c >= col or board[r][c] != word[index] or (r,c) in visited:
                return False
            if index == len(word) - 1:
                return True
            visited.add((r,c))
            res = dfs(r + 1, c, index+1) or dfs(r - 1, c, index+1) or dfs(r, c + 1, index+1) or dfs(r, c - 1, index+1) 
            visited.remove((r,c))
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False
