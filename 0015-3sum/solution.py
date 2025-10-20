class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result =  []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, n-1
            while lo<hi:
                curr = nums[i]+nums[lo]+nums[hi]
                if curr>0:
                    hi-=1
                elif curr <0:
                    lo+=1
                else:
                    result.append([nums[i],nums[lo],nums[hi]])
                    lo,hi=lo+1,hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo+=1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi-=1
        
        return result
