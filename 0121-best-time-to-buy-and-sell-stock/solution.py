class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price,max_profit = prices[0],0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price =  prices[i]
            else:
                max_profit = max(max_profit, prices[i]- min_price)
        return max_profit

