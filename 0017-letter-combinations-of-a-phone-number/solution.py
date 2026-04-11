class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        result = []
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
        def backtrack(index,path):
            if index == n:
                result.append("".join(path))
                return
            strs = my_map[digits[index]]
            for ch in strs:
                path.append(ch)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return result

