class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_sub = 0
        left = 0
        window_map = defaultdict(int)
        for i in range(n):
            window_map[fruits[i]]+=1
            if len(window_map) > 2:
                while len(window_map) > 2:
                    window_map[fruits[left]] -=1
                    if window_map[fruits[left]] <= 0:
                        del window_map[fruits[left]]
                    left += 1
            max_sub = max(max_sub, i - left + 1)
        return max_sub

