class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_s1 = Counter(s1)
        map_s2 = defaultdict(int)
        n = len(s2)
        m = len(s1)
        left = 0
        for i in range(n):
            map_s2[s2[i]] +=1
            if map_s2 == map_s1:
                return True
            if i - left + 1 >=m:
                while i-left + 1>=m:
                    map_s2[s2[left]] -=1
                    if map_s2[s2[left]] <=0:
                        del map_s2[s2[left]]
                    left+=1
        return False
