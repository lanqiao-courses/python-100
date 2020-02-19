class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception('Stack is full')
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception('Stack is empty')
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[stack_index] -= 1
        return data