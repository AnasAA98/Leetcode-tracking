class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            my_map[key].append(word)
        return [my_map[k] for k in my_map]

