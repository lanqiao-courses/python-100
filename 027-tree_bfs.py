from bst import Bst
from collections import deque


class BstBfs(Bst):

    def bfs(self, visit_func):
        if self.root is None:
            raise TypeError('root is None')
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            visit_func(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)