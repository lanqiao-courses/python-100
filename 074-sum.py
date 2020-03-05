class Solution(object):

    def sum_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b;
        carry = (a&b) << 1
        if carry != 0:
            return self.sum_two(result, carry)
        return result