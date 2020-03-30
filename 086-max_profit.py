class Solution(object):

    def find_max_profit(self, prices):
        if prices is None:
            raise TypeError('prices cannot be None')
        if len(prices) < 2:
            raise ValueError('prices must have at least two values')
        min_price = prices.pop(0)
        max_profit = prices[0] - min_price
        for price in prices:
            profit = price - min_price
            min_price = min(price, min_price)
            max_profit = max(profit, max_profit)
        return max_profit