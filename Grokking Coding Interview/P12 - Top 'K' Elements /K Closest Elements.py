from heapq import *

def find_closest_elements(arr, K, X):
  result = []
  minHeap = []
  index = binSClosest(arr, X)
  low, high = max(0, index-K), min(len(arr)-1, index+K)

  for x in range(low, high+1):
      heappush(minHeap, (abs(X-arr[x]), arr[x]))

  for _ in range(K):
      result.append(heappop(minHeap)[1])

  return result

def binSClosest(arr, target):
  start, end = 0, len(arr)-1
  closest = float('-inf')
  index = None

  while start < end:
      mid = start +(end-start)/2
      mid = int(mid)

      if abs(target-arr[mid]) > closest:
          closest = abs(target-arr[mid])
          index = mid

      if arr[mid] == target:
            return mid

      elif arr[mid] > target:
          end = mid - 1

      else:
          start = mid + 1


  return start




def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()