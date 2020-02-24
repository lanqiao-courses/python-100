class InsertionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1:r+1] = data[l:r]
                    data[l] = temp
        return data