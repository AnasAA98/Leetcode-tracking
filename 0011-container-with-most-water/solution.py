class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_volume = 0
        while left<right:
            curr_volume = (right - left) * min(height[left],height[right])
            max_volume = max(max_volume,curr_volume)
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return max_volume


