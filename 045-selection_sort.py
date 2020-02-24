class SelectionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]
        return data