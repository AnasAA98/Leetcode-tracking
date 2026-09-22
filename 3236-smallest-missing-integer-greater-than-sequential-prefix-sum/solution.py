class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        my_set = set(nums)
        seq = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] == seq[-1] + 1:
                seq.append(nums[i])
            else:
                break
        curr_sum = sum(seq)
        while curr_sum in my_set:
            curr_sum += 1
        
        return curr_sum

