class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def explore(r, c, index):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in seen
                or word[index] != board[r][c]
            ):
                return False
            if index == len(word) - 1:
                return True
            seen.add((r, c))
            check = (
                explore(r + 1, c, index + 1)
                or explore(r - 1, c, index + 1)
                or explore(r, c + 1, index + 1)
                or explore(r, c - 1, index + 1)
            )
            seen.remove((r, c))
            return check

        res = False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    res = res or explore(i, j, 0) 
        return res

