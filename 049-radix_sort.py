class RadixSort(object):

    def sort(self, array, base=10):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return []
        max_element = max(array)
        max_digits = len(str(abs(max_element)))
        curr_array = array
        for digit in range(max_digits):
            buckets = [[] for _ in range(base)]
            for item in curr_array:
                buckets[(item//(base**digit))%base].append(item)
            curr_array = []
            for bucket in buckets:
                curr_array.extend(bucket)
        return curr_array