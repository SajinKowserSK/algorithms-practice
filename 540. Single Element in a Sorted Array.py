'''Title:540. Single Element in a Sorted Array
Difficulty: Medium
Description: Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once.
Find this single element that appears only once.''' 





class Solution(object):
    def singleNonDuplicate(self, nums):

        if len(nums) == 1:
            return nums[0]

        elif len(nums) == 0:
            return 0

        for x in range (1, len(nums)-1):

            if nums[x] != nums[x+1] and nums[x] != nums[x-1]:
                return nums[x]

            elif nums[0] != nums[1]:
                return nums[0]

            elif nums[-1] != nums[-2]:
                return nums[-1]

