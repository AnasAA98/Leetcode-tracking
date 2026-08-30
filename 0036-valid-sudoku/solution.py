class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_row = set()
        set_col = set()
        set_sqr = set()
        # row check
        for i in range(9):
            for j in range(9):
                if board[i][j] in set_row:
                    return False
                elif board[i][j] == '.':
                    continue
                else:
                    set_row.add(board[i][j])
            set_row.clear()

        # column check
        for i in range(9):
            for j in range(9):
                if board[j][i] in set_col:
                    return False
                elif board[j][i] == '.':
                    continue
                else:
                    set_col.add(board[j][i])
            set_col.clear()

        
        # square check
        for r in range(0,9,3):
            for c in range(0,9,3):
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] in set_sqr:
                            return False
                        elif board[i][j] == '.':
                            continue
                        else:
                            set_sqr.add(board[i][j])
                set_sqr.clear()
        return True
