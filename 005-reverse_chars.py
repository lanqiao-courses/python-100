class ReverseString(object):

    def reverse(self, chars):
        if chars:
            size = len(chars)
            for i in range(size // 2):
                chars[i], chars[size - 1 - i] = \
                    chars[size - 1 - i], chars[i]
        return chars