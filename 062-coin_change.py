class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            return None
        if not coins or total == 0:
            return 0
        coins = [0] + coins
        num_rows = len(coins)
        num_cols = total + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0:
                    T[i][j] = 0
                    continue
                if j == 0:
                    T[i][j] = 1
                    continue
                if coins[i] <= j:
                    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
                else:
                    T[i][j] = T[i - 1][j]
        return T[num_rows - 1][num_cols - 1]