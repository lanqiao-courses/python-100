class Solution(object):

    def merge_ranges(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return array
        sorted_array = sorted(array)
        merged_array = [sorted_array[0]]
        for index, item in enumerate(sorted_array):
            if index == 0:
                continue
            start_prev, end_prev = merged_array[-1]
            start_curr, end_curr = item
            if end_prev < start_curr:
                # No overlap, add the entry
                merged_array.append(item)
            else:
                # Overlap, update the previous entry's end value
                merged_array[-1] = (start_prev, max(end_prev, end_curr))
        return merged_array