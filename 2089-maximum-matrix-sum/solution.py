class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count_neg = 0
        min_val = float("inf")
        total_sum = 0
        for row in matrix:
            for val in row:
                if val < 0:
                    count_neg +=1
                x = abs(val)
                min_val = min(min_val,x)
                total_sum+=abs(val)
        if count_neg % 2 == 0:
            return total_sum
        return total_sum - 2 * min_val
