class Solution(object):
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        contig_sum = nums[0]

        for x in range(1, len(nums)):
            curr = nums[x]

            contig_sum = curr + contig_sum

            if contig_sum < curr:
                contig_sum = curr

            max_sum = max(contig_sum, max_sum)

        return max_sum


