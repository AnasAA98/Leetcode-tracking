class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        # group the unique numbers with their indices
        for i,n in enumerate(nums):
            groups[n].append(i)
        res = [0] * len(nums)
        for key, indices in groups.items():
            total_sum = sum(indices)
            left_sum = 0
            left_coun = 0
            for index, pos in enumerate(indices):
                right_sum = total_sum - left_sum - pos
                right_count = len(indices) - 1 - index 
                pre_sum = pos * index - left_sum
                suf_sum = right_sum - right_count * pos
                res[pos] = pre_sum + suf_sum
                left_sum += pos
        return res

