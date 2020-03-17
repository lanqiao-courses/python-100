class Bits(object):

    def get_next_largest(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num <= 0:
            raise ValueError('num cannot be 0 or negative')
        num_ones = 0
        num_zeroes = 0
        num_copy = num
        # We'll look for index, which is the right-most non-trailing zero
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 0:
            num_zeroes += 1
            num_copy >>= 1
        # Count number of ones to the right of index
        while num_copy != 0 and num_copy & 1 == 1:
            num_ones += 1
            num_copy >>= 1
        # Determine index and set the bit
        index = num_zeroes + num_ones
        num |= 1 << index
        # Clear all bits to the right of index
        num &= ~((1 << index) - 1)
        # Set bits starting from 0
        num |= ((1 << num_ones - 1) - 1)
        return num

    def get_next_smallest(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num <= 0:
            raise ValueError('num cannot be 0 or negative')
        num_ones = 0
        num_zeroes = 0
        num_copy = num
        # We'll look for index, which is the right-most non-trailing one
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 1:
            num_ones += 1
            num_copy >>= 1
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 0:
            num_zeroes += 1
            num_copy >>= 1
        # Determine index and clear the bit
        index = num_zeroes + num_ones
        num &= ~(1 << index)
        # Clear all bits to the right of index
        num &= ~((1 << index) - 1)
        # Set bits starting from 0
        num |= (1 << num_ones + 1) - 1
        return num