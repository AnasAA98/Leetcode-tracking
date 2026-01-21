class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        top, bottom = 0, rows-1
        r = -1
        while top<= bottom:
            mid_row = (top + bottom)  // 2
            if matrix[mid_row][-1] < target:
                top = mid_row + 1
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                r = mid_row
                break
        
        if r == -1:
            return False
        lo,hi = 0,cols -1
        while lo <= hi:
            mid = (lo+hi) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                hi = mid -1
            else:
                lo = mid + 1
        return False

            
