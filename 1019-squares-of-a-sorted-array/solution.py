class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        index = n - 1
        result = [0] * n
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left >= right:
                result[index] = left *left
                l += 1
            else:
                result[index] = right * right
                r -= 1
            index -= 1
        return result

