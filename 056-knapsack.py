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
        num_rows = len(input_items)
        num_cols = total_weight + 1
        T = [0] * (num_cols)
        for i in range(num_rows):
            for j in range(num_cols):
                if j >= input_items[i].weight:
                    T[j] = max(input_items[i].value + T[j - input_items[i].weight],
                               T[j])
        return T[-1]