class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def explore(r, c, index):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if board[r][c] != word[index]:
                return False
            if index == n - 1:
                return True
            temp = board[r][c]
            board[r][c] = "#"
            found = (explore(r+1, c, index+1) or explore(r-1, c, index+1) or explore(r, c+1, index+1) or explore(r, c-1, index+1))
            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and explore(i, j, 0):
                    return True

        return False

