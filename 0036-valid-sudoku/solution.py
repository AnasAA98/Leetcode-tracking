class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        set_rows = set()
        set_cols = set()
        set_squares = set()
        # check rows
        for i in range(9):
            for j in range(9):
                if grid[i][j] == ".":
                    continue
                elif grid[i][j] in set_rows:
                    return False
                else:
                    set_rows.add(grid[i][j])
            set_rows.clear()
        # check columns
        for i in range(9):
            for j in range(9):
                if grid[j][i] == ".":
                    continue
                elif grid[j][i] in set_cols:
                    return False
                else:
                    set_cols.add(grid[j][i])
            set_cols.clear()
        # check squares
        for square_r in range(0,9,3):
            for square_c in range(0,9,3):
                for i in range(square_r,square_r+3):
                    for j in range(square_c,square_c+3):
                        if grid[i][j] == ".":
                            continue
                        elif grid[i][j] in set_squares:
                            return False
                        else:
                            set_squares.add(grid[i][j])
                set_squares.clear()
        return True
