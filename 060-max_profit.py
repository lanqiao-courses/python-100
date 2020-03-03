from enum import Enum
import sys


class Type(Enum):
    SELL = 0
    BUY = 1


class Transaction(object):

    def __init__(self, type, day, price):
        self.type = type
        self.day = day
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and \
            self.day == other.day and \
            self.price == other.price

    def __repr__(self):
        return str(self.type) + ' day: ' + \
            str(self.day) + ' price: ' + \
            str(self.price)


class StockTrader(object):

    def find_max_profit(self, prices, k):
        if prices is None or k is None:
            raise TypeError('prices or k cannot be None')
        if not prices or k <= 0:
            return []
        num_rows = k + 1  # 0th transaction for dp table
        num_cols = len(prices)
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                    continue
                max_profit = -sys.maxsize
                for m in range(j):
                    profit = prices[j] - prices[m] + T[i - 1][m]
                    if profit > max_profit:
                        max_profit = profit
                T[i][j] = max(T[i][j - 1], max_profit)
        return self._find_max_profit_transactions(T, prices)

    def _find_max_profit_transactions(self, T, prices):
        results = []
        i = len(T) - 1
        j = len(T[0]) - 1
        max_profit = T[i][j]
        while i != 0 and j != 0:
            if T[i][j] == T[i][j - 1]:
                j -= 1
            else:
                sell_price = prices[j]
                results.append(Transaction(Type.SELL, j, sell_price))
                profit = T[i][j] - T[i - 1][j - 1]
                i -= 1
                j -= 1
                for m in range(j + 1)[::-1]:
                    if sell_price - prices[m] == profit:
                        results.append(Transaction(Type.BUY, m, prices[m]))
                        break
        return (max_profit, results)