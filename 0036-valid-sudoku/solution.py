class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_rows = set()
        set_cols = set()
        set_squares = set()

        # check row duplicate
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!= "." and board[i][j] in set_rows:
                    return False
                elif board[i][j]== ".":
                    continue
                else:
                    set_rows.add(board[i][j])
            set_rows.clear()
        
        # check col duplicate
        for j in range(0,9):
            for i in range(0,9):
                if board[i][j]!= "." and board[i][j] in set_cols:
                    return False
                elif board[i][j]== ".":
                    continue
                else:
                    set_cols.add(board[i][j])
            set_cols.clear()

        # check square duplicate
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                for i in range(row_box,row_box+3):
                    for j in range(col_box,col_box+3):
                        if board[i][j] == '.':
                            continue
                        elif board[i][j] in set_squares:
                            return False
                        else:
                            set_squares.add(board[i][j])
                set_squares.clear()
        return True
