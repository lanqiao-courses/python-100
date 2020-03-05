class Solution(object):

    def __init__(self, upper_limit=100):
        self.max = None
        self.min = None
        # Mean
        self.num_items = 0
        self.running_sum = 0
        self.mean = None
        # Mode
        self.array = [0] * (upper_limit + 1)
        self.mode_occurrences = 0
        self.mode = None

    def insert(self, val):
        if val is None:
            raise TypeError('val cannot be None')
        if self.max is None or val > self.max:
            self.max = val
        if self.min is None or val < self.min:
            self.min = val
        # Calculate the mean
        self.num_items += 1
        self.running_sum += val
        self.mean = self.running_sum / self.num_items
        # Calculate the mode
        self.array[val] += 1
        if self.array[val] > self.mode_occurrences:
            self.mode_occurrences = self.array[val]
            self.mode = val