from stack import Stack
import sys


class StackMin(Stack):

    def __init__(self, top=None):
        super(StackMin, self).__init__(top)
        self.stack_of_mins = Stack()

    def minimum(self):
        if self.stack_of_mins.top is None:
            return sys.maxsize
        else:
            return self.stack_of_mins.peek()

    def push(self, data):
        super(StackMin, self).push(data)
        if data < self.minimum():
            self.stack_of_mins.push(data)

    def pop(self):
        data = super(StackMin, self).pop()
        if data == self.minimum():
            self.stack_of_mins.pop()
        return data