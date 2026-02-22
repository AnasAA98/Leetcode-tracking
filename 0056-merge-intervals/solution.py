class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda items:items[0])
        result = [sorted_list[0]]
        for i in range(1,len(sorted_list)):
            if result[-1][1] >= sorted_list[i][0]:
                result[-1][1] = max(result[-1][1],sorted_list[i][1])
            else:
                result.append(sorted_list[i])
        return result
