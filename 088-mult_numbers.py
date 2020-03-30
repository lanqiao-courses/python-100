class Solution(object):

    def mult_other_numbers(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return array
        if len(array) == 1:
            return []
        result = []
        for i in range(len(array)):
            curr_sum = 1
            for j in range(len(array)):
                if i == j:
                    continue
                curr_sum *= array[j]
            result.append(curr_sum)
        return result