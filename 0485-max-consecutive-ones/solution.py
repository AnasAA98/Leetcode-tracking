class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0
        for x in nums:
            if x==1:
                curr_ones+=1
                max_ones = max(curr_ones,max_ones)

            else:
                curr_ones = 0
        return max_ones
