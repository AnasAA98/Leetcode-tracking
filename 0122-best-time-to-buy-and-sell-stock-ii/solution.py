class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # either buy or sell the stock
        # you can only hold at most one share 
        # chasing short term gain 
        n = len(prices)
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, n):
            if buy_price > prices[i]:
                buy_price = prices[i]
            else:
                max_profit+= prices[i]-buy_price
                buy_price = prices[i]
        return max_profit
