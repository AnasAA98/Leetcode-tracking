class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [-1] * n 
        right = [-1] * n
        inter = [-1] * n
        max_val = -1
        for i in range(n):
            left[i] = max_val
            max_val = max(max_val,height[i]) # update the boundary to keep left biggest boundary
        max_val = -1
        for i in range(n-1,-1,-1):
            right[i] = max_val
            max_val = max(max_val,height[i])
        # get the smallest boundary at any level i for both left and right
        for i in range(n):
            inter[i] = min(left[i],right[i])
        # check now if we can trap water
        res = 0
        for i in range(n):
            curr = inter[i] - height[i]
            if curr > 0:
                res += curr
        return res
