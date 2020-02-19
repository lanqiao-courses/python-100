from stack import Stack


class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        super(StackWithCapacity, self).__init__(top)
        self.capacity = capacity
        self.num_items = 0

    def push(self, data):
        if self.is_full():
            raise Exception('Stack full')
        super(StackWithCapacity, self).push(data)
        self.num_items += 1

    def pop(self):
        self.num_items -= 1
        return super(StackWithCapacity, self).pop()

    def is_full(self):
        return self.num_items == self.capacity

    def is_empty(self):
        return self.num_items == 0


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = []
        self.last_stack = None

    def push(self, data):
        if self.last_stack is None or self.last_stack.is_full():
            self.last_stack = StackWithCapacity(None, self.indiv_stack_capacity)
            self.stacks.append(self.last_stack)
        self.last_stack.push(data)

    def pop(self):
        if self.last_stack is None:
            return None
        data = self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data