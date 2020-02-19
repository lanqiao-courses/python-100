class Solution(object):

    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError('nums or target cannot be None')
        if not nums:
            raise ValueError('nums cannot be empty')
        cache = {}
        for index, num in enumerate(nums):
            cache_val = val - num
            if num in cache:
                return [cache[num], index]
            else:
                cache[cache_val] = index
        return None