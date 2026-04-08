class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / k)
            if curr_hours <= h:
                res = min (res, k)
                right = k - 1
            else:
                left = k + 1
        return res
