class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # generate all subsets:
        result =[[]]
        for num in nums:
            subset =[]
            for curr_sub in result:
                subset.append(curr_sub+[num])
            result.extend(subset)
        total = 0
        for i in result:
            curr = 0
            for j in i:
                curr = curr ^ j
            total += curr
        return total
