class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = 0
        n = len(shifts)
        for i in range(n-1,-1,-1):
            prefix += shifts[i]
            shifts[i] = prefix
        result = []
        shift = 0
        for i in range(n):
            shift = shifts[i] % 26
            if shift + ord(s[i]) > ord('z'):
                j = ord('z') - ord(s[i]) + 1
                shift = shift - j
                result.append(chr(ord('a')+ shift))
            else:
                result.append(chr(ord(s[i])+ shift))
        return "".join(result)
