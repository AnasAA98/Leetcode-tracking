class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            sort_map[sorted_word].append(word)
        return [val for k,val in sort_map.items()]
