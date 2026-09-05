class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        for price in prices:
            minprice = min(minprice,price)
            profit = max(profit,price-minprice)
        return profit
        