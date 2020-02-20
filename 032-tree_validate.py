from bst import Bst
import sys


class BstValidate(Bst):

    def validate(self):
        if self.root is None:
            raise TypeError('No root node')
        return self._validate(self.root)

    def _validate(self, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if node is None:
            return True
        if node.data <= minimum or node.data > maximum:
            return False
        if not self._validate(node.left, minimum, node.data):
            return False
        if not self._validate(node.right, node.data, maximum):
            return False
        return True