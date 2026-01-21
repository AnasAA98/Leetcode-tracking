class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col = len(matrix),len(matrix[0])
        #intialize the boundaries
        top_row = 0
        bottom_row = row -1
        left_col = 0
        right_col =  col -1
        result = []
        while left_col <= right_col and top_row <= bottom_row:
            # clear out top row
            for d in range(left_col,right_col+1):
                result.append(matrix[top_row][d])
            top_row+=1
            # clear out right col
            for d in range(top_row,bottom_row+1):
                result.append(matrix[d][right_col])
            right_col -=1
            
            # clear out bottom row
            if top_row <= bottom_row:
                for d in range(right_col,left_col -1, -1):
                    result.append(matrix[bottom_row][d])
                bottom_row -=1
            
            # clear out left col
            if left_col <= right_col:
                for d in range(bottom_row,top_row -1,-1):
                    result.append(matrix[d][left_col])
                left_col +=1
        return result
                    
            
        
