def validate_index(func):
    def validate_index_wrapper(self, *args, **kwargs):
        for arg in args:
            if arg < 0:
                raise IndexError('Invalid index')
        return func(self, *args, **kwargs)
    return validate_index_wrapper


class Bit(object):

    def __init__(self, number):
        if number is None:
            raise TypeError('number cannot be None')
        self.number = number

    @validate_index
    def get_bit(self, index):
        mask = 1 << index
        return self.number & mask != 0

    @validate_index
    def set_bit(self, index):
        mask = 1 << index
        self.number |= mask
        return self.number

    @validate_index
    def clear_bit(self, index):
        mask = ~(1 << index)
        self.number &= mask
        return self.number

    @validate_index
    def clear_bits_msb_to_index(self, index):
        mask = (1 << index) - 1
        self.number &= mask
        return self.number

    @validate_index
    def clear_bits_index_to_lsb(self, index):
        mask = ~((1 << index + 1) - 1)
        self.number &= mask
        return self.number

    @validate_index
    def update_bit(self, index, value):
        if value is None or value not in (0, 1):
            raise Exception('Invalid value')
        if self.get_bit(index) == value:
            return self.number
        if value:
            self.set_bit(index)
        else:
            self.clear_bit(index)
        return self.number