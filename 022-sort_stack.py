from stack import Stack

class MyStack(Stack):

    def sort(self):
        buff = MyStack()
        while not self.is_empty():
            temp = self.pop()
            while not buff.is_empty() and temp < buff.peek():
                self.push(buff.pop())
            buff.push(temp)
        return buff