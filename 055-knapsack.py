class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


class Knapsack(object):

    def fill_knapsack(self, input_items, total_weight):
        if input_items is None or total_weight is None:
            raise TypeError('input_items or total_weight cannot be None')
        if not input_items or total_weight == 0:
            return 0
        items = list([Item(label='', value=0, weight=0)] + input_items)
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                elif j >= items[i].weight:
                    T[i][j] = max(items[i].value + T[i - 1][j - items[i].weight],
                                  T[i - 1][j])
                else:
                    T[i][j] = T[i - 1][j]
        results = []
        i = num_rows - 1
        j = num_cols - 1
        while T[i][j] != 0:
            if T[i - 1][j] ==  T[i][j]:
                i -= 1
            elif T[i][j - 1] ==  T[i][j]:
                j -= 1
            else:
                results.append(items[i])
                i -= 1
                j -= items[i].weight
        return results