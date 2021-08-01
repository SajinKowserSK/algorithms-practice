def find_duplicate(nums):
  start = 0

  while start < len(nums):
    currValRightIndex = nums[start] - 1

    # put the number where it needs to be
    if nums[start] != nums[currValRightIndex]:
      nums[start], nums[currValRightIndex] = nums[currValRightIndex], nums[start]

    else:
      start += 1

  for x in range(len(nums)):
    if nums[x] != x + 1:
      return nums[x]

  return -1