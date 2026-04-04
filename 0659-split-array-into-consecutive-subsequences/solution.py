class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = defaultdict(int)
        for k in nums:
            if freq[k] == 0:
                continue
            elif need[k] > 0:
                freq[k] -= 1
                need[k] -= 1
                need[k+1] += 1
            elif need[k] == 0:
                if freq[k+1] > 0 and freq[k+2] > 0:
                    freq[k] -= 1
                    freq[k+1] -= 1  
                    freq[k+2] -= 1
                    need[k+3] += 1
                else:
                    return False
        return True
