def count_rotations(arr):
  return (findMax(arr)+1) % len(arr)


def findMax(arr):
  start, end = 0, len(arr)-1
  LM = arr[0]

  while start < end:
    mid = start + (end-start) // 2
    if arr[mid-1] < arr[mid] > arr[mid+1]:
      return mid

    else:
      if arr[mid] >= LM:
        # ascending so go right
        start = mid + 1

      else:
        # descending as start is greater -> go left
        end = mid - 1

  return start


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
