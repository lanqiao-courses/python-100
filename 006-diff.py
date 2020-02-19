class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')
        result = 0
        for char in str1:
            result ^= ord(char)
        for char in str2:
            result ^= ord(char)
        return chr(result)