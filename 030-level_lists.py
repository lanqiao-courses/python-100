from bst import Bst


class BstLevelLists(Bst):

    def create_level_lists(self):
        if self.root is None:
            return
        results = []
        current = []
        parents = []
        current.append(self.root)
        while current:
            results.append(current)
            parents = list(current)
            current = []
            for parent in parents:
                if parent.left is not None:
                    current.append(parent.left)
                if parent.right is not None:
                    current.append(parent.right)
        return results