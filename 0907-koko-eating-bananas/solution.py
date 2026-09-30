class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles) # largest pile to be consumed in an hour
        
        # minimum speed to finish all piles in h
        k = math.inf
        
        while left <= right:
            # find my candidate speed 
            cand_speed = (left + right) // 2
            curr = 0
            # need to check if with candidate speed koko can finish before h hours
            for pile in piles:
                # we use math.ceil since if there's a remeinder such that .6 we  need a whole hour to finish that 0.6 
                curr += math.ceil(pile / cand_speed)
            if curr > h:
                # means we need to increase eating speed
                left = cand_speed + 1
            else:
                right = cand_speed - 1
                k = min(k, cand_speed)
        
        return k


