class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            left, right = 0, len(intervals)
            while left<right:
                mid = (left + right) //2
                if intervals[mid][0] < newInterval[0]:
                    left = mid +1
                else:
                    right = mid
            intervals.insert(left, newInterval)
            return self.merge(intervals)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            result = [intervals[0]]
            for i in range (1,len(intervals)):
                if intervals[i][0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1],intervals[i][1])
                else:
                    result.append(intervals[i])
            return result


