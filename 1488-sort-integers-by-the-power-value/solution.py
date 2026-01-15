class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1:0}
        result = []
        
        for i in range(lo,hi+1):
            val = i 
            hist = []
            curr_steps = 0
            while val != 1 and val not in cache:
                hist.append(val)
                if val % 2 == 0:
                    val //= 2
                else:
                    val = 3 * val + 1
                curr_steps +=1
            curr_steps+= cache[val]
            result.append((i,curr_steps))
            total = cache[val]
            for x in reversed(hist):
                total+=1
                cache[x] = total
        output = sorted(result, key=lambda x:(x[1],x[0]))
        return output[k-1][0]

