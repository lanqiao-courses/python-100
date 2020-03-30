class Solution(object):

    def move_zeroes(self, nums):
        if nums is None:
            raise TypeError('nums cannot be None')
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        if pos < len(nums):
            nums[pos:] = [0] * (len(nums) - pos)