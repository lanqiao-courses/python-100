class Parentheses(object):

    def find_pair(self, num_pairs):
        if num_pairs is None:
            raise TypeError('num_pairs cannot be None')
        if num_pairs < 0:
            raise ValueError('num_pairs cannot be < 0')
        if not num_pairs:
            return []
        results = []
        curr_results = []
        self._find_pair(num_pairs, num_pairs, curr_results, results)
        return results

    def _find_pair(self, nleft, nright, curr_results, results):
        if nleft == 0 and nright == 0:
            results.append(''.join(curr_results))
        else:
            if nleft >= 0:
                self._find_pair(nleft-1, nright, curr_results+['('], results)
            if nright > nleft:
                self._find_pair(nleft, nright-1, curr_results+[')'], results)