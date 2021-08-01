def find_missing_number(nums):
    # numbers from 0 to N
    # N will be out of the index's range
    # we need to make sure that for each index, i, nums[i] = i
    # however we know nums[i] for the index N won't make sense so we can just skip it
    # basically we will have all the numnbers where it should be except for the N, it will be in the index that is missing so return the index
    # if that index were to come back, it would've swapped out for N later in the iteration

    start = 0
    while start < len(nums):
        currValCorrectIndex = nums[start]
        if nums[start] < len(nums) and nums[start] != start:
            nums[start], nums[currValCorrectIndex] = nums[currValCorrectIndex], nums[start]

        else:
            start += 1

    for x in range(0, len(nums)):
        if nums[x] != x:
            return x

    return -1

# def find_missing_number(nums):
#   right_sum = 0
#   for x in range(0, len(nums)+1):
#     right_sum += x

#   curr_sum = 0

#   for elem in nums:
#     curr_sum += elem

#   return right_sum - curr_sum


#
# # first glance
# def find_missing_number(nums):
#     right_sum = 0
#     for x in range(0, len(nums) + 1):
#         right_sum += x
#
#     curr_sum = 0
#
#     for elem in nums:
#         curr_sum += elem
#
#     return right_sum - curr_sum