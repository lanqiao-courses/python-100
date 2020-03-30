class Solution(object):

    def max_xor(self, lower, upper):
        result = 0
        for l in range(lower, upper + 1):
            for u in range(lower, upper + 1):
                curr = l ^ u
                if result < curr:
                    result = curr
        return result