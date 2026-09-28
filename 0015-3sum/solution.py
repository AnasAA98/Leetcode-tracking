class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

