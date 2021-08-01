def find_corrupt_numbers(nums):
  start = 0
  while start < len(nums):
    rightIndex = nums[start]-1
    if nums[start] != nums[rightIndex]:
      nums[start], nums[rightIndex] = nums[rightIndex], nums[start]
    else:
      start += 1

  for x in range(0, len(nums)):
    if nums[x] != x + 1:
      return [nums[x], x+1]
  return [-1, -1]
