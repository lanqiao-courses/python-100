class Solution(object):

    def can_win_nim(self, num_stones_left):
        return num_stones_left % 4 != 0