class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            speed = (left + right) // 2  
            hours = 0
            for i in range(len(piles)):
                hours += (piles[i] + speed - 1) // speed
            if hours <= h:
                right = speed - 1
                res = min(res, speed)
            else:
                left = speed + 1
        return res

