class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        # initialize the boundaries (they will change according to the spirale logic)
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        result = []
        while left <= right and top <= bottom:
            # clearing out the top row by going left --> right
            for d in range(left,right+1):
                result.append(matrix[top][d])
            top+=1
            # clearing out the right col by going top --> bottom
            for d in range(top,bottom+1):
                result.append(matrix[d][right])
            right-=1

            """ 
            clearing the bottom row by going right --> left
            since top has been updated but we are still in while loop
            need to check if the top <= bottom condition still holds
            """
            if top <= bottom:
                for d in range(right,left-1,-1):
                    result.append(matrix[bottom][d])
                bottom -=1
            

            # clearing out the left col follwoing same logic
            if left<=right:
                for d in range(bottom,top-1,-1):
                    result.append(matrix[d][left])
                left+=1
        return result
