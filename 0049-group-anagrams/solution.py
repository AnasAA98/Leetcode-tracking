class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for wrd in strs:
            count = [0] * 26
            for ch in wrd:
                count[ord(ch) - ord('a')] +=1
            my_map[tuple(count)].append(wrd)
        return list(my_map.values())
