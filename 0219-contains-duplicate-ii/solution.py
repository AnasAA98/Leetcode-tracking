class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dic = {}
        for i,num in enumerate(nums):
            if num in my_dic and abs(i - my_dic[num]) <= k:
                return True
            my_dic[num] = i
        return False
