class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            k = (left + right) // 2 # candiate speed
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / k)
            if curr_h <= h:
                res = min(res,k)
                right = k - 1
            else:
                left = k + 1
        return res

