class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        res = []
        rem = finalSum
        i = 2
        while i <= rem:
            res.append(i)
            rem -= i
            i += 2
        res[-1] += rem
        return res

