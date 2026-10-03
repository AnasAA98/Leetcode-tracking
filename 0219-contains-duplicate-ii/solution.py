class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l = 0
        res = set()
        for i in range(len(nums)):
            if len(res) > k:
                res.remove(nums[i - k - 1])
            if nums[i] in res:
                return True
            res.add(nums[i])
        return False
