class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows -1):
            row = [0]+result[-1]+[0]
            temp =[]
            for j in range(len(result[-1])+1):
                temp.append(row[j]+row[j+1])
            result.append(temp)
        return result
                
