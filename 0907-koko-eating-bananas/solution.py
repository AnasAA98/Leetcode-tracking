class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            k = (left+right) // 2 # candidate speed
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / k) # number of hours needed to finish each pile
            if curr_h > h:
                left = k + 1
            else:
                res = min(res,k) # valid speed K, need to update my result
                right = k - 1
        return res

