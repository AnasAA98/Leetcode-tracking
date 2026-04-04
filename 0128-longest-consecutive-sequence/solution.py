class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        max_seq = 0
        for k in seq:
            if k-1 in seq:
                continue
            else:
                i = k
                curr = 1
                while i in seq:
                    max_seq = max(curr,max_seq)
                    i+=1
                    curr+=1
        return max_seq



                
