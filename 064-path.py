class Grid(object):

    def find_path(self, matrix):
        if matrix is None or not matrix:
            return None
        cache = {}
        path = []
        if self._find_path(matrix, len(matrix) - 1,
                           len(matrix[0]) - 1, cache, path):
            return path
        else:
            return None

    def _find_path(self, matrix, row, col, cache, path):
        if row < 0 or col < 0 or not matrix[row][col]:
            return False
        cell = (row, col)
        if cell in cache:
            return cache[cell]
        cache[cell] = (row == 0 and col == 0 or
                       self._find_path(matrix, row, col - 1, cache, path) or
                       self._find_path(matrix, row - 1, col, cache, path))
        if cache[cell]:
            path.append(cell)
        return cache[cell]