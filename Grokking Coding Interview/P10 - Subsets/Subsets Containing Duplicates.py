class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subsets.append([])

        if len(subsets) == 0:
            return subsets

        start, end = 0, 0

        for x in range(0, len(nums)):
            start = 0

            if x > 0 and nums[x] == nums[x - 1]:
                start = end + 1  # end has not been updated after the last nums' copies. This means end + 1 is the head of the last added.

            end = len(subsets) - 1  # last element

            for y in range(start, end + 1):
                elem = subsets[y]
                elem = elem.copy()
                elem.append(nums[x])
                subsets.append(elem)

        return subsets
