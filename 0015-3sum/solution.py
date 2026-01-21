class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n):
            l,r = i+1,n-1
            while l<r:
                current_sum = nums[i]+nums[l] + nums[r]
                if current_sum > 0:
                    r-=1
                elif current_sum < 0:
                    l+=1
                else:
                    result.add((nums[i],nums[l] ,nums[r]))
                    l+=1
                    r-=1
        return [list(t) for t in result]
