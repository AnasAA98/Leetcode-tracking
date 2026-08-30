class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        res = 0
        while left <= right:
            curr = (right - left) * min(height[right],height[left])
            res = max(res, curr)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res

