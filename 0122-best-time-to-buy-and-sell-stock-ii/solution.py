class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # either buy or sell the stock
        # you can only hold at most one share 
        # chasing short term gain 
        n = len(prices)
        max_profit = 0
        min_profit = prices[0]
        for i in range(1,n):
            if prices[i]< min_profit:
                min_profit = prices[i]
            else:
                max_profit+= prices[i]-min_profit
                min_profit = prices[i]
        return max_profit

