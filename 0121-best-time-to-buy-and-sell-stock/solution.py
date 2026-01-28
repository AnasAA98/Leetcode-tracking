class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can only buy in day[i] and sell in day[j]
        # where i<j
        n =  len(prices)
        min_price = prices[0]
        max_price = 0
        for i in range(1,n):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                max_price = max(max_price,prices[i]-min_price)
        return max_price

