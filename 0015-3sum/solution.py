class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n -1
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr == 0 :
                    result.append([nums[left],nums[right], nums[i]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    left+=1
                    right-=1
                elif curr < 0:
                    left+=1
                else:
                    right-=1
        return result 
