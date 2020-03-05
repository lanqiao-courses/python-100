class Solution(object):

    def is_power_of_two(self, val):
        if val is None:
            raise TypeError('n cannot be None')
        if val <= 0:
            return False
        return (val & (val - 1)) == 0