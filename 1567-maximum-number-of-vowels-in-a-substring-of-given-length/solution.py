class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        curr_vowels = 0
        max_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                curr_vowels+=1
        max_vowels = curr_vowels
        if max_vowels == k:
            return max_vowels
        for idx in range(k,n):
            if s[idx] in vowels:
                curr_vowels +=1
            if s[idx-k] in vowels:
                curr_vowels-=1
            max_vowels = max(max_vowels,curr_vowels)
        return max_vowels

