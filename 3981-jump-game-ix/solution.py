class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = [] # entries are (start_index, max_value)
        for i in range(n):
            start = i
            curr_max = nums[i]
            # we only merge back when the curr max is smaller than the previous max 
            while stack and nums[i] < stack[-1][1]:
                prev_start,prev_max = stack.pop()
                start = prev_start
                curr_max = max(curr_max,prev_max)
            stack.append((start,curr_max))
        #populate ans
        while stack:
            curr_start,curr_max= stack.pop()
            while curr_start <= n - 1 and ans[curr_start] == -1:
                ans[curr_start] = curr_max
                curr_start += 1
        return ans



                


