class Solution(object):

    def add_digits(self, val):
        if val is None:
            raise TypeError('num cannot be None')
        if val < 0:
            raise ValueError('num cannot be negative')
        digits = []
        while val != 0:
            digits.append(val % 10)
            val //= 10
        digits_sum = sum(digits)
        if digits_sum >= 10:
            return self.add_digits(digits_sum)
        else:
            return digits_sum