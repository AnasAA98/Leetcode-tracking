class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
        sorted_map = sorted(map.items(), key=lambda item:item[1],reverse = True)
        result = []
        for key,v in sorted_map:
            if k == 0:
                break
            result.append(key)
            k-=1
        return result
