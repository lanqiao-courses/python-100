class Bits(object):

    def insert_m_into_n(self, m, n, i, j):
        if None in (m, n, i, j):
            raise TypeError('Argument cannot be None')
        if i < 0 or j < 0:
            raise ValueError('Index cannot be negative')
        left_mask = -1 << (j + 1)
        right_mask = (1 << i) - 1
        n_mask = left_mask | right_mask
        # Clear bits from j to i, inclusive
        n_cleared = n & n_mask
        # Shift m into place before inserting it into n
        m_left = m << i
        left_mask_new = ~left_mask
        m_mask = m_left & left_mask_new
        return n_cleared | m_mask