class Solution(object):
    def findMin(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        rightMost = nums[-1]

        while start < end:
            mid = int((start + end) / 2)

            if mid == len(nums) - 1 and nums[mid - 1] > nums[mid] or nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[
                mid]:
                return nums[mid]

            elif nums[mid] < rightMost:  # have to go left since from mid to rightMost is > mid
                return self.findMin(nums[0:mid])

            else:  # when right most is geat
                return self.findMin(nums[mid + 1::])

        return nums[start]

