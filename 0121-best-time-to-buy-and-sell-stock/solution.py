class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price = prices[0],0
        for i in range(1,len(prices)):
            
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                max_price = max(max_price, prices[i]-min_price)
        return max_price
