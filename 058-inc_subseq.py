class Subsequence(object):

    def longest_inc_subseq(self, seq):
        if seq is None:
            raise TypeError('seq cannot be None')
        if not seq:
            return []
        temp = [1] * len(seq)
        prev = [None] * len(seq)
        for r in range(1, len(seq)):
            for l in range(r):
                if seq[l] < seq[r]:
                    if temp[r] < temp[l] + 1:
                        temp[r] = temp[l] + 1
                        prev[r] = l
        max_val = 0
        max_index = -1
        results = []
        for index, value in enumerate(temp):
            if value > max_val:
                max_val = value
                max_index = index
        curr_index = max_index
        while curr_index is not None:
            results.append(seq[curr_index])
            curr_index = prev[curr_index]
        return results[::-1]