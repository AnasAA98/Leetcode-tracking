class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set() #  (r,c) 
        def dfs (r,c,index) -> bool:
            if  r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in visited or board[r][c] != word[index] :
                return False
            if index == len(word) - 1:
                return True
            visited.add((r,c))
            res = (dfs(r-1,c,index + 1) or dfs (r+1,c,index + 1) or dfs (r,c-1,index + 1) or dfs (r,c+1,index + 1))
            visited.remove((r,c))
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False
