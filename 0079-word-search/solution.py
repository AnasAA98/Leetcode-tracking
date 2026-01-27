class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board),len(board[0])
        visited = set()
        n = len(word)
        def dfs(r,c,index):
            if r < 0 or c <0 or r>=rows or c>=cols or (r,c) in visited or board[r][c] != word[index]:
                return False
            if index == n-1:
                return True
            visited.add((r,c))
            next_cell = (dfs(r+1,c,index+1)or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1))
            visited.remove((r,c))
            return next_cell        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False
