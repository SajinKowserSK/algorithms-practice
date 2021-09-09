from heapq import *

def find_sum_of_elements(nums, k1, k2):
  minHeap = []
  for elem in nums:
    heappush(minHeap, elem)

  for _ in range(k1):
    heappop(minHeap)

  counter = k1
  elem_sum = 0

  while counter < k2-1:
    elem_sum += heappop(minHeap)
    counter += 1

  return elem_sum


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
