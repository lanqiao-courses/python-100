class Solution(object):

    def length_longest_path(self, file_system):
        if file_system is None:
            raise TypeError('file_system cannot be None')
        max_len = 0
        path_len = {0: 0}
        for line in file_system.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len