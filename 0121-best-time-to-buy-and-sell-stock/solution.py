class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                res = max (res, price - min_price)
        return res 
