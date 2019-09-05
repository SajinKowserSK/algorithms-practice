class Solution(object):
    def search(self, nums, target):
        if len(nums) > 0 and target in nums:
            return nums.index(target)

        else:
            return -1
