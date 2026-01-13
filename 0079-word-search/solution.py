class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n = len(word)
        rows, cols = len(board), len(board[0])

        def explore(i, j, index):
            if (
                i >= rows
                or i < 0
                or j >= cols
                or j < 0
                or board[i][j] != word[index]
                or (i, j) in visited
            ):
                return False
            if index == n - 1:
                return True
            visited.add((i, j))
            next_cell = (
                explore(i + 1, j, index + 1)
                or explore(i - 1, j, index + 1)
                or explore(i, j + 1, index + 1)
                or explore(i, j - 1, index + 1)
            )
            visited.remove((i, j))
            return next_cell

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and explore(i, j,0):
                    return True
        return False

