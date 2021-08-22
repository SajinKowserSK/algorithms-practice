def binary_search(arr, key):
  asc = arr[0] < arr[-1]
  start, end = 0, len(arr)-1

  while start <= end:
    mid = int((start+end)/2)
    if arr[mid] == key:
      return mid


    if asc:
      if arr[mid] > key:
        end = mid - 1

      else:
        start = mid + 1

    else:
      if arr[mid] > key:
        start = mid + 1

      else:
        end = mid - 1

  return -1



def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()
