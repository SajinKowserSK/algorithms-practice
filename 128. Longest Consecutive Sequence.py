class Solution(object):
    def longestConsecutive(self, nums):
        nums = list(dict.fromkeys(nums))
        nums.sort()
        counter = 0
        subs = []

        for x in range(0, len(nums) - 1):
            if nums[x + 1] == nums[x] + 1:
                counter = counter + 1

            else:
                subs.append(counter + 1)
                counter = 0

        subs.append(counter + 1)
        if len(nums) == 0:
            return 0

        elif len(subs) > 0:
            return max(subs)

        elif len(nums) == 1:
            return 0

        else:
            return 0
