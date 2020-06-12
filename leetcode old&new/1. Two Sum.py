class Solution(object):
    def twoSum(self, nums, target):
        returnList = [];

        for x in range(0, len(nums)):
            for y in range(x + 1, len(nums)):

                if nums[x] + nums[y] == target:
                    returnList.append(x)
                    returnList.append(y)

        return returnList
