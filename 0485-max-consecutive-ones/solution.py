class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        curr = 0
        for d in nums:
            if d == 1:
                curr+=1
                max_num = max(curr,max_num)
            else:
                curr = 0
        return max_num
