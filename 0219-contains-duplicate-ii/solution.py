class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}
        for i,num in enumerate(nums):
            if num in check and (abs(i - check[num]) <= k):
                return True
            check[num] = i
        return False
