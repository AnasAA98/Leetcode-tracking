class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = math.inf
        while left <= right:
            candidate_speed = (left + right) // 2
            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / candidate_speed)
            if curr_hours <= h :
                res = min(candidate_speed,res)
                right = candidate_speed - 1
            else:
                left = candidate_speed + 1
        return res
