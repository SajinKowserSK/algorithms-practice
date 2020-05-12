class Solution(object):
    def dominantIndex(self, nums):
        num2 = nums[:]
        num2.sort()
        largest = max(nums)
        ret = True

        for x in range(0, len(num2) - 1):
            if largest >= num2[x] * 2:
                ret = True

            else:
                ret = False

        if ret == False:
            return -1

        else:
            return nums.index(largest)

