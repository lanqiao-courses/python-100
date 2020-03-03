class Steps(object):

    def count_ways(self, num_steps):
        if num_steps is None or num_steps < 0:
            raise TypeError('num_steps cannot be None or negative')
        cache = {}
        return self._count_ways(num_steps, cache)

    def _count_ways(self, num_steps, cache):
        if num_steps < 0:
            return 0
        if num_steps == 0:
            return 1
        if num_steps in cache:
            return cache[num_steps]
        cache[num_steps] = (self._count_ways(num_steps-1, cache) +
                            self._count_ways(num_steps-2, cache) +
                            self._count_ways(num_steps-3, cache))
        return cache[num_steps]