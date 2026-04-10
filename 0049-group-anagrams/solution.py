class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for wrd in strs:
            key = "".join(sorted(wrd))
            my_map[key].append(wrd)
        return [val for k,val in my_map.items()]

