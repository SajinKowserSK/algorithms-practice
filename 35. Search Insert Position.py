class Solution(object):
    def searchInsert(self, nums, target):

        if target in nums:
            return nums.index(target)

        elif target > nums[-1]:
            return len(nums)

        elif target < nums[0]:
            return 0

        else:
            for x in range(0, len(nums) - 1):
                if nums[x] < target and nums[x + 1] > target:
                    return x + 1
