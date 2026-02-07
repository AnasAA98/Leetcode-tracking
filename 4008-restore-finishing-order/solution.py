class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        for num in order:
            if num in friends:
                res.append(num)
        return res
