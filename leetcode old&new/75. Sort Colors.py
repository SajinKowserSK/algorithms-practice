class Solution:
    def sortColors(self, nums: List[int]) -> None:

        elements = len(nums)

        if elements < 2:
            return nums

        frontier = 0

        for x in range(1, elements):
            if nums[x] <= nums[0]:
                frontier += 1

                tmp = nums[x]
                nums[x] = nums[frontier]
                nums[frontier] = tmp

        tmp = nums[0]
        nums[0] = nums[frontier]
        nums[frontier] = tmp

        print(nums)

        left = self.sortColors(nums[0:frontier])
        right = self.sortColors(nums[frontier + 1:elements])

        nums = left + [nums[frontier]] + right

        return nums

        """
        Do not return anything, modify nums in-place instead.
        """
