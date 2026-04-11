class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0
        for num in seq:
            if num -1 in seq: # not start of a sequence
                continue
            else:
                i = num
                size = 1
                while i in seq :
                    res = max(res,size)
                    i+=1
                    size +=1
        return res
