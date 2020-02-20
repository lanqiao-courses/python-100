from bst import Bst


class Solution(Bst):

    def find_second_largest(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        if self.root.right is None and self.root.left is None:
            raise ValueError('root must have at least one child')
        return self._find_second_largest(self.root)

    def _find_second_largest(self, node):
        if node.right is not None:
            if node.right.left is not None or node.right.right is not None:
                return self._find_second_largest(node.right)
            else:
                return node
        else:
            return self._find_right_most_node(node.left)

    def _find_right_most_node(self, node):
        if node.right is not None:
            return self._find_right_most_node(node.right)
        else:
            return node