class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        res = 0
        left = 0
        for i in range (len(fruits)):
            basket[fruits[i]]+=1
            if len(basket) > 2:
                while len(basket) > 2:
                    basket[fruits[left]] -= 1
                    if basket[fruits[left]] == 0:
                        del basket[fruits[left]]
                    left += 1
            res = max (res, i - left + 1)
        return res


