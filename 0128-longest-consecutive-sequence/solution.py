class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        best = 0
        # key here is to look for start of the consecutive sequence 
        for x in set_nums:
            if x - 1 not in set_nums:
                curr = 0
                start = x
                while start in set_nums:
                    start+=1
                    curr +=1
                    best = max(curr,best)
        return best
