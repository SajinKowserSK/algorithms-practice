class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]

        elif nums.count(target) == 1:
            return [nums.index(target), nums.index(target)]

        indices = [i for i, x in enumerate(nums) if x == target]
        start = min(indices)
        stop = max(indices)
        return [start, stop]






