class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if n < m:
            return []
        p_count = Counter(p)
        window_map = defaultdict(int)
        result = []
        left = 0
        for i in range(n):
            window_map[s[i]]+=1
            if window_map == p_count:
                result.append(left)
            if i-left+1 >= m:
                while i-left+1 >= m:
                    window_map[s[left]]-=1
                    if window_map[s[left]] <= 0:
                        del window_map[s[left]]
                    left+=1
        return result      


            


        
