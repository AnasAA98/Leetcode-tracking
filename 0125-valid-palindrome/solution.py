class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = s.lower()
        clean = "".join(ch for ch in s if ch.isalnum())
        result = list(clean)
        return result == result[::-1]

