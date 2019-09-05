class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        retL = []
        for x in nums:
            if x not in retL:
                retL.append(x)

        if len(retL) >= 3:
            return retL[-3]

        else:
            return max(nums)
