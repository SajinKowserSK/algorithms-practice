class Solution(object):
    def containsDuplicate(self, nums):
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True

        return False

