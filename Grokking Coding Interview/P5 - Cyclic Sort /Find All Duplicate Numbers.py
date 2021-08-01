def find_all_duplicates(nums):
  duplicateNumbers = []
  start = 0

  while start < len(nums):
    correct_i = nums[start] - 1

    if nums[start] != nums[correct_i]:
      nums[start], nums[correct_i] = nums[correct_i], nums[start]

    else:
      start += 1

  for x in range(0, len(nums)):
    if nums[x] != x + 1:
      duplicateNumbers.append(nums[x])


  return duplicateNumbers