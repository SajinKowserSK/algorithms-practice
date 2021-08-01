def cyclic_sort(nums):
    start = 0

    while start < len(nums):
        correct_index = nums[start] - 1
        swap(start, correct_index, nums)

        if nums[start] == start + 1:
            start += 1

    return nums

    return nums


def swap(i1, i2, nums):
    tmp = nums[i1]
    nums[i1] = nums[i2]
    nums[i2] = tmp
