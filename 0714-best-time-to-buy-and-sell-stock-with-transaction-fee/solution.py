class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            curr_price = price - min_price
            if curr_price > fee:   # there is profit to make here in this situation
                max_profit += price - min_price - fee
                min_price = price -fee
            elif min_price > price:
                min_price = price
        return max_profit
