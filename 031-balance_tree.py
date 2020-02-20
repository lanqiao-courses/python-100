from bst import Bst


class BstBalance(Bst):

    def check_balance(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        height = self._check_balance(self.root)
        return height != -1

    def _check_balance(self, node):
        if node is None:
            return 0
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1
        diff = abs(left_height - right_height)
        if diff > 1:
            return -1
        return 1 + max(left_height, right_height)