class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right
        while left <= right:
            mid = (left + right) // 2 # candidate cap
            curr_days = 1
            curr_cap = 0
            for wei in weights:
                curr_cap += wei
                if curr_cap  > mid:
                    curr_days +=1
                    curr_cap = wei
            if curr_days <= days:
                right = mid - 1
                res = min(res,mid)
            else:
                 left = mid + 1
        return res
