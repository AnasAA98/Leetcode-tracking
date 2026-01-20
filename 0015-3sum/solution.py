class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i-1]:
                continue
            lo = i + 1
            hi = n - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum > 0:
                    hi-=1
                elif curr_sum < 0:
                    lo+=1
                else:
                    result.add((nums[i] ,nums[lo] ,nums[hi]))
                    hi-=1
                    lo+=1
        return [list(key) for key in result]
