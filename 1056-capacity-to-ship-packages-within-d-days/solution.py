class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            # curr capacity
            mid_cap = (low+ high) // 2
            curr_capacity = 0
            start_day = 1
            for w in weights:
                if curr_capacity + w <= mid_cap:
                    curr_capacity+=w
                else:
                    start_day +=1
                    curr_capacity = w
            if start_day <= days:
                high = mid_cap
            else:
                low = mid_cap +1
        return low

