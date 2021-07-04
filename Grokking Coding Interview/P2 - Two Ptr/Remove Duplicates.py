class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        nondups = 1
        for j in range(i + 1, len(nums)):
            if nums[j] != nums[i]:
                nondups += 1
                nums[i + 1] = nums[j]
                i = i + 1

        return nondups
