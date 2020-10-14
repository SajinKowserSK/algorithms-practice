def maxSubArray(nums):
    if nums is None or len(nums) == 0:
        return None

    max_sum = nums[0]
    contig = nums[0]

    for x in range(1, len(nums)):

        curr = nums[x]  # 4
        both = contig + curr  # 3

        if both > curr:
            contig = both

        else:
            contig = curr  # 4

        max_sum = max(max_sum, contig)

    return max_sum

# TEST CASES
# print(maxSubArray([-1,4,5,-7,3])) # 9
# print(maxSubArray([-1,-1,-2])) # -1
