class Solution(object):

    def find_content_children(self, greed_indices, cookie_sizes):
        if greed_indices is None or cookie_sizes is None:
            raise TypeError('greed_indices or cookie_sizes cannot be None')
        if not greed_indices or not cookie_sizes:
            return 0
        greed_indices.sort()
        cookie_sizes.sort()
        greed_index = 0
        num_children = 0
        for size in cookie_sizes:
            if greed_index >= len(greed_indices):
                break
            if size >= greed_indices[greed_index]:
                num_children += 1
                greed_index += 1
        return num_children