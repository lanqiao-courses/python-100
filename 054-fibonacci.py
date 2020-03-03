class Math(object):

    def fib_recursive(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_iterative(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def fib_dynamic(self, n):
        cache = {}
        return self._fib_dynamic(n, cache)

    def _fib_dynamic(self, n, cache):
        if n == 0 or n == 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self._fib_dynamic(n-1, cache) + self._fib_dynamic(n-2, cache)
        return cache[n]