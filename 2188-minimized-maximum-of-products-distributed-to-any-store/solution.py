class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        left = 1
        right = max(quantities)

        res = right 
        while left <= right:
            # most any single store is allowed to hold
            cand = (left + right) // 2
            # curr_stores that are full
            curr_stores = 0
            for q in quantities:
                # number of stores that q take up 
                curr_stores += math.ceil(q/cand)
            if curr_stores > n:
                # need an increased cap:
                left = cand + 1
            else:
                res = min(res, cand)
                right = cand - 1
        return res 


