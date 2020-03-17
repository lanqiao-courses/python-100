class Bits(object):

    def bits_to_flip(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        count = 0
        c = a ^ b
        while c:
            count += c & 1
            c >>= 1
        return count