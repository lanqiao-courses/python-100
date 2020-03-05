class Solution(object):

    def sub_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b
        borrow = (~a & b) << 1
        if borrow != 0:
            return self.sub_two(result, borrow)
        return result