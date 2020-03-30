class Solution(object):

    def count_sentence_fit(self, sentence, rows, cols):
        if sentence is None:
            raise TypeError('sentence cannot be None')
        if rows is None or cols is None:
            raise TypeError('rows and cols cannot be None')
        if rows < 0 or cols < 0:
            raise ValueError('rows and cols cannot be negative')
        if cols == 0 or not sentence:
            return 0
        curr_row = 0
        curr_col = 0
        count = 0
        while curr_row < cols:
            for word in sentence:
                # If the current word doesn't fit on the current line,
                # move to the next line
                if len(word) > cols - curr_col:
                    curr_col = 0
                    curr_row += 1
                # If we are beyond the number of rows, return
                if curr_row >= rows:
                    return count
                # If the current word fits on the current line,
                # 'insert' it here
                if len(word) <= cols - curr_col:
                    curr_col += len(word) + 1
                # If it still doesn't fit, then the word is too long
                # and we should just return the current count
                else:
                    return count
            count += 1
        return count