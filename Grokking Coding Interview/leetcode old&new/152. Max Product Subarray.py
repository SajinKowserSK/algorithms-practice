class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        max_product = nums[0]
        min_product = nums[0]
        prev_max_product = nums[0]
        prev_min_product = nums[0]

        for x in range(1, len(nums)):
            max_product = max(prev_max_product * nums[x], prev_min_product * nums[x], nums[x])
            min_product = min(prev_max_product * nums[x], prev_min_product * nums[x], nums[x])
            result = max(max_product, result)
            prev_max_product = max_product
            prev_min_product = min_product

        return result

