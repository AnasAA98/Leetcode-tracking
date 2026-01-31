class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        set_rows = set()
        set_cols = set()
        set_squares = set()
        # check for rows
        for i in range(9):
            for j in range(9):
                if grid[i][j] == '.':
                    continue
                if grid[i][j] in set_rows:
                    return False
                set_rows.add(grid[i][j])
            set_rows.clear()
        for i in range(9):
            for j in range(9):
                if grid[j][i] == '.':
                    continue
                if grid[j][i] in set_cols:
                    return False
                set_cols.add(grid[j][i])
            set_cols.clear()
        for square_r in range(0,9,3):
            for square_c in range(0,9,3):
                for i in range(square_r,square_r+3):
                    for j in range(square_c,square_c+3):
                        if grid[i][j] == '.':
                            continue
                        if grid[i][j] in set_squares:
                            return False
                        set_squares.add(grid[i][j])
                set_squares.clear()
        return True
