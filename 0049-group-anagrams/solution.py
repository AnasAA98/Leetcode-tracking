class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        result = []
        for word in strs:
            temp = ''.join(sorted(word))
            map[temp].append(word)
        for key in map:
            result.append(map[key])
        return result
