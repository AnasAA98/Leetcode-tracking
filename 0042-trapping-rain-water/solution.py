class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left = [-1] * n
        right = [-1] * n
        
        max_val = -1
        for i in range(n):
            left[i] = max_val
            max_val = max(max_val,height[i])
        
        max_val = -1
        for i in range(n -1, -1, -1):
            right[i] = max_val
            max_val = max(max_val, height[i])
        
        res = 0
        for i in range(n):
            curr = min(right[i],left[i]) - height[i]
            if curr > 0 :
                res += curr

        return res 

