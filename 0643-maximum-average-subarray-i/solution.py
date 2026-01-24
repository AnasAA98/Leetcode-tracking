class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == k:
            return sum(nums) / k
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k,n):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum,curr_sum)
        return max_sum / k
