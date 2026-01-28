class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        result = []
        path = []
        my_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def explore(index):
            if index == n :
                result.append("".join(path))
                return
            
            number = my_map[digits[index]]
            for ch in number:
                path.append(ch)
                explore(index+1)
                path.pop()
        explore(0)
        return result
