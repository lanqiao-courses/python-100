import sys


class Matrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second


class MatrixMultiplicationCost(object):

    def find_min_cost(self, matrices):
        if matrices is None:
            raise TypeError('matrices cannot be None')
        if not matrices:
            return 0
        size = len(matrices)
        T = [[0] * size for _ in range(size)]
        for offset in range(1, size):
            for i in range(size-offset):
                j = i + offset
                min_cost = sys.maxsize
                for k in range(i, j):
                    cost = (T[i][k] + T[k+1][j] +
                            matrices[i].first *
                            matrices[k].second *
                            matrices[j].second)
                    if cost < min_cost:
                        min_cost = cost
                T[i][j] = min_cost
        return T[0][size-1]