class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=set()
        n=len(nums)
        for i in range(n):
            if nums[i]>0: break
            if i and nums[i]==nums[i-1]: continue
            l,r=i+1,n-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s<0: l+=1
                elif s>0: r-=1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1; r-=1
        return [list(t) for t in res]

