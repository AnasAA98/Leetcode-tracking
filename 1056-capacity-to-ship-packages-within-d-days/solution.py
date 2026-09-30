class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = 1
        right = sum(weights)
        
        res = math.inf

        while left <= right:
            cand_cap = (left + right) // 2
            curr_days = 1
            curr_cap = 0
            for w in weights:
                curr_cap += w
                if curr_cap > cand_cap and w <= cand_cap:
                    curr_days += 1
                    curr_cap = w
                elif w > cand_cap:
                    curr_days = days + 1
                    break
            if curr_days > days:
                left = cand_cap + 1
            else:
                res = min(res, cand_cap)
                right = cand_cap - 1
        return res 

                   




