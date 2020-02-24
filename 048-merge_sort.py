class MergeSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = self._sort(left)
        right = self._sort(right)
        return self._merge(left, right)

    def _merge(self, left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # Copy remaining elements
        while l < len(left):
            result.append(left[l])
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1
        return result