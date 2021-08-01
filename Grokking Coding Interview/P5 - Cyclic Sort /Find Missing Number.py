# first glance
def find_missing_number(nums):
    right_sum = 0
    for x in range(0, len(nums) + 1):
        right_sum += x

    curr_sum = 0

    for elem in nums:
        curr_sum += elem

    return right_sum - curr_sum