class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = math.inf
        while left <= right:
            mid = (left + right) // 2 # candidate speed
            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / mid) 
                # for each pile divide it by candidate speed if total takes 3.1 hours then it means take 4 hours to finish set pile
            if curr_hours <= h:
                min_speed = min(min_speed, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_speed
                

