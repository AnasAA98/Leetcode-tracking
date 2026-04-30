class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse = True)
        prev = math.inf
        res = 0
        for cap in maximumHeight:
            prev = min(prev-1,cap)
            if prev <= 0:
                return -1
            res += prev

        return res
