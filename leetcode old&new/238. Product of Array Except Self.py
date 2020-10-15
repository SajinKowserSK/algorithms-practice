class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        L, R, ans = [], [], []
        L.append(1)
        R.insert(0, 1)

        for x in range(1, len(nums)):
            L.append(nums[x - 1] * L[-1])

        for y in range(len(nums) - 2, -1, -1):
            R.insert(0, nums[y + 1] * R[0])

        for z in range(0, len(L)):
            ans.append(L[z] * R[z])

        return ans
