class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        key = [0] * 26
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord('a') - ord(ch)] +=1
            key = tuple(count)
            my_map[key].append(word)
        return list(my_map.values())

