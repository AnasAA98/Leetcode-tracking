class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            l,r = i+1,n-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
        return [list(x) for x in res]
        

