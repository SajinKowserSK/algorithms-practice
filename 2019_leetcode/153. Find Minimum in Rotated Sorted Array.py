class Solution(object):
    def findMin(self, nums):
        nums.sort()
        if len(nums) > 0:
            return min(nums)
