class StringCompare(object):

    def longest_common_subseq(self, str0, str1):
        if str0 is None or str1 is None:
            raise TypeError('str input cannot be None')
        # Add one to number of rows and cols for the dp table's
        # first row of 0's and first col of 0's
        num_rows = len(str0) + 1
        num_cols = len(str1) + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                elif str0[j - 1] != str1[i - 1]:
                    T[i][j] = max(T[i][j - 1],
                                  T[i - 1][j])
                else:
                    T[i][j] = T[i - 1][j - 1] + 1
        results = ''
        i = num_rows - 1
        j = num_cols - 1
        # Walk backwards to determine the subsequence
        while T[i][j]:
            if T[i][j] == T[i][j - 1]:
                j -= 1
            elif T[i][j] == T[i - 1][j]:
                i -= 1
            elif T[i][j] == T[i - 1][j - 1] + 1:
                results += str1[i - 1]
                i -= 1
                j -= 1
            else:
                raise Exception('Error constructing table')
        # Walking backwards results in a string in reverse order
        return results[::-1]