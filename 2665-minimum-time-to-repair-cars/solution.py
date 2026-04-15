class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1 # 1 car 1 mechanic ranked 1
        high = max(ranks) * (cars ** 2) # the time it takes if that worst mechanic fixed ALL the cars alone
        res = math.inf
        while low <= high:
            mid = (low + high) //2 
            total_cars = 0
            for rank in ranks:
                total_cars += int(sqrt(mid/rank))
            if total_cars < cars:
                low = mid + 1
            else:
                res = min(res, mid) # candidate time
                high = mid - 1

        return res

