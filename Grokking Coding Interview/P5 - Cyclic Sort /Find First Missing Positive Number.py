def find_first_smallest_missing_positive(nums):

  start = 0
  while start < len(nums):
    rightIndex = nums[start] - 1

    # we have to put the current numbers in their place
    # however only for positive numbers and numbers within the range 1 to N
    if nums[start] > 0 and rightIndex <= len(nums) and nums[start] != nums[rightIndex]:
      nums[start], nums[rightIndex] = nums[rightIndex], nums[start]

    else:
      start += 1

  for x in range(0, len(nums)-1):
    curr = nums[x]
    nextnum = nums[x+1]

    if curr > 0 and nextnum != curr + 1:
      return curr + 1



  return -1

tsts = [[-3, 1, 5, 4, 2], [3, -2, 0, 1, 2], [3, 2, 5, 1]]
for tst in tsts:
    print(find_first_smallest_missing_positive(tst))