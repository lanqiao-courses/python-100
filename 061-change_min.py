import sys


class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            raise TypeError('coins or total cannot be None')
        if not coins or total == 0:
            return 0
        cache = {}
        return self._make_change(coins, total, cache)

    def _make_change(self, coins, total, cache):
        if total == 0:
            return 0
        if total in cache:
            return cache[total]
        min_ways = sys.maxsize
        for coin in coins:
            if total - coin < 0:
                continue
            ways = self._make_change(coins, total - coin, cache)
            if ways < min_ways:
                min_ways = ways
        cache[total] = min_ways + 1
        return cache[total]