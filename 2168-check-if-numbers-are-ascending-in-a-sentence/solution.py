class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        array = s.split()
        res = []
        prev = -1
        for word in array:
            if word.isdigit():
                if prev >= int(word):
                    return False
                else:
                    prev = int(word)
        return True
                

