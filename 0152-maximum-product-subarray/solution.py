class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -inf
        curr_min = 1
        curr_max = 1
        for n in nums:
            x,y =curr_max,curr_min
            curr_max = max(n * x, n * y, n)
            curr_min = min(n * x, n * y, n)
            res = max(res,curr_max,curr_min)
        return res        
