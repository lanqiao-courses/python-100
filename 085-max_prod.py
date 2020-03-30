class Solution(object):

    def max_prod_three(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if len(array) < 3:
            raise ValueError('array must have 3 or more ints')
        array.sort()
        product = 1
        for item in array[-3:]:
            product *= item
        return product