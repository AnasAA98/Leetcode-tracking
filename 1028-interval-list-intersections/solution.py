class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a = max(firstList[i][0],secondList[j][0])
            b = min (firstList[i][1], secondList[j][1])
            if a<= b:
                res.append([a,b])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return res

