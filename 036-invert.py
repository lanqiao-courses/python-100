from bst import Bst


class InverseBst(Bst):

    def invert_tree(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        return self._invert_tree(self.root)

    def _invert_tree(self, root):
        if root is None:
            return
        self._invert_tree(root.left)
        self._invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root