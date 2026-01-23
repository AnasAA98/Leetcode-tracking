class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            curr_sub = []
            for subsets in result:
                curr_sub.append(subsets+[num])
            result.extend(curr_sub)
        return result
