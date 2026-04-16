class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = max(ranks) * (cars**2)
        res = math.inf
        while low <= high:
            candidate = (low + high) // 2 # mins
            num_cars = 0
            for rank in ranks:
                num_cars += int(sqrt(candidate / rank))
            if num_cars < cars:
                low = candidate + 1 # number of mins not enough to clear out all cars
            else:
                res = min(res,candidate)
                high = candidate - 1
        return res



            


