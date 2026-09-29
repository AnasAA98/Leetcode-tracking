class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = math.inf
        while left <= right :
            curr_speed = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / curr_speed)
            if hours > h:
                left = curr_speed + 1
            else :
                res = min (res, curr_speed)
                right = curr_speed - 1
        return res
