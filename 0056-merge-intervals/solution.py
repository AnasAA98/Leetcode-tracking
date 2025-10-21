class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda item:item[0])
        # print(sorted_intervals)
        result = [sorted_intervals[0]]
        for i in range (1,len(sorted_intervals)):
            if sorted_intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1],sorted_intervals[i][1])
            else:
                result.append(sorted_intervals[i])
        return result 

