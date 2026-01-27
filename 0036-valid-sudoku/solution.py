class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        """
        3 main conditions:  - rows contain unique ints
                            - cols contain unique ints
                            - each 3*3 board contain unique ints
        use sets for uniqueness if any value already in a set then return false
        """
        set_rows = set()
        set_cols = set()
        set_squares = set()
        # check for values in rows
        for i in range(0,9):
            for j in range(0,9):
                if grid[i][j] == '.':
                    continue
                elif grid[i][j] in set_rows:
                    return False
                set_rows.add(grid[i][j])
            set_rows.clear()
        # check for values in cols:
        for i in range(0,9):
            for j in range(0,9):
                if grid[j][i] == '.':
                    continue
                elif grid[j][i] in set_cols:
                    return False
                set_cols.add(grid[j][i])
            set_cols.clear()
        # check for values in square:
        for square_r in range(0,9,3):
            for square_c in range(0,9,3):
                for i in range(square_r,square_r+3):
                    for j in range(square_c,square_c+3):
                        if grid[i][j] == '.':
                            continue
                        elif grid[i][j] in set_squares:
                            return False
                        set_squares.add(grid[i][j])
                set_squares.clear()
        return True

