class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0]
        
        for curr in intervals[1:]:
            # if start of curr interv is less than ending of prev interv we have an overlap
            if curr[0] < prev[1]:
                # drop one interv
                res +=1
                # need to update my prev by dropping the interv with the highest ending time (greedy)
                prev = curr if curr[1] < prev[1] else prev 
            else:
                # simply update prev to the new iterv
                prev = curr
        return res     
