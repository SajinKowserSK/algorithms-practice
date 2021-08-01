def find_missing_numbers(nums):
  missingNumbers = []
  start = 0
  while start < len(nums):

    print(nums, start)
    currValRightIndex = nums[start] - 1

    # since there are duplicates we just need to make sure that before moving on that
    # whatever is in our current_value , the correct position in the array for that current_value is fulfilled
    # therefore current_value = nums[start] then nums[start] == nums[nums[start]-1] before moving on

    if nums[start] != nums[currValRightIndex]:
      nums[start], nums[currValRightIndex] = nums[currValRightIndex], nums[start]

    else:
      start += 1

  for x in range(len(nums)):
      if nums[x] != x+1:
          missingNumbers.append(x+1)
  return missingNumbers



  return missingNumbers


print(find_missing_numbers([3, 3, 3, 3, 2, 3, 5, 1]))